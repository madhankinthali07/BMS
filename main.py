import os
import logging
from contextlib import asynccontextmanager
from typing import List, Optional
from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from sqlalchemy.orm import Session

from config import settings, save_smtp_settings
from database import init_db, get_db
from models import (
    AlertTask, ShowRecord, NotificationLog,
    TrackerCreateRequest, TrackerResponse, TestEmailRequest, SMTPSettingsRequest
)
from scrapers import bms_scraper, district_scraper, simulator_scraper
from notifiers.email_service import email_service
from monitor import monitor_service

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("CineAlert")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize Database and Start Background Monitor
    init_db()
    await monitor_service.start()
    logger.info("Application started. Background monitor active.")
    yield
    # Shutdown: Stop Background Monitor
    await monitor_service.stop()
    logger.info("Application shutdown complete.")

app = FastAPI(
    title=settings.APP_NAME,
    description="Real-time BookMyShow & District Showtimes Tracker and Instant Email Notifier",
    version="1.0.0",
    lifespan=lifespan
)

templates = Jinja2Templates(directory="templates")

# --- UI Route ---

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": settings.APP_NAME,
            "smtp_configured": email_service.is_configured(),
            "sender_email": email_service.sender_email
        }
    )

# --- Trackers Endpoints ---

@app.get("/api/trackers", response_model=List[TrackerResponse])
def get_trackers(db: Session = Depends(get_db)):
    tasks = db.query(AlertTask).order_by(AlertTask.created_at.desc()).all()
    return tasks

@app.post("/api/trackers", response_model=TrackerResponse, status_code=status.HTTP_201_CREATED)
def create_tracker(payload: TrackerCreateRequest, db: Session = Depends(get_db)):
    new_task = AlertTask(
        platform=payload.platform,
        city=payload.city.strip().lower(),
        movie_name=payload.movie_name.strip(),
        movie_code=payload.movie_code.strip() if payload.movie_code else "",
        theater_name=payload.theater_name.strip(),
        venue_code=payload.venue_code.strip() if payload.venue_code else "",
        target_date=payload.target_date.strip(),
        format_filter=payload.format_filter or "ALL",
        user_email=payload.user_email.strip(),
        check_interval=max(settings.MIN_CHECK_INTERVAL, payload.check_interval or settings.DEFAULT_CHECK_INTERVAL),
        is_active=True,
        status_message="Tracker registered, monitoring active."
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    logger.info(f"Created new tracker #{new_task.id} for {new_task.movie_name}")
    return new_task

@app.post("/api/trackers/{tracker_id}/toggle")
def toggle_tracker(tracker_id: int, db: Session = Depends(get_db)):
    task = db.query(AlertTask).filter(AlertTask.id == tracker_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tracker not found")
    task.is_active = not task.is_active
    task.status_message = "Active - Monitoring" if task.is_active else "Paused by user"
    db.commit()
    return {"success": True, "is_active": task.is_active, "status_message": task.status_message}

@app.post("/api/trackers/{tracker_id}/check")
async def trigger_manual_check(tracker_id: int):
    result = await monitor_service.check_task_now(tracker_id)
    return result

@app.post("/api/trackers/{tracker_id}/simulate-drop")
def simulate_show_drop(tracker_id: int, db: Session = Depends(get_db)):
    """
    Demo / Simulation tool: generates a simulated newly opened showtime
    and immediately sends a real-time email alert to the user.
    """
    task = db.query(AlertTask).filter(AlertTask.id == tracker_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tracker not found")

    import random
    times = ["07:15 PM (Prime)", "10:30 PM (Late Night)", "03:45 PM (Matinee)"]
    simulated_time = random.choice(times)
    m_upper = (task.movie_name or "").strip().upper()
    is_any_movie = (
        not m_upper or 
        m_upper in ["ALL", "ANY", "*", "ALL MOVIES", "ANY MOVIE"] or 
        "ANY MOVIE" in m_upper or 
        "ALL MOVIES" in m_upper
    )
    sim_movie = "Scene (UA16+)" if is_any_movie else task.movie_name
    simulated_show = [{
        "show_id": f"sim_drop_{datetime.utcnow().timestamp()}",
        "platform": task.platform.upper(),
        "movie_name": sim_movie,
        "theater_name": task.theater_name,
        "show_time": simulated_time,
        "format_type": "IMAX 2D" if "imax" in task.theater_name.lower() else "Dolby Atmos 2D",
        "price_info": "₹450 - ₹750",
        "status": "AVAILABLE",
        "booking_url": "https://in.bookmyshow.com" if "bms" in task.platform.lower() else "https://www.district.in"
    }]

    # Save to shows
    rec = ShowRecord(
        task_id=task.id,
        show_id=simulated_show[0]["show_id"],
        platform=simulated_show[0]["platform"],
        show_time=simulated_show[0]["show_time"],
        format_type=simulated_show[0]["format_type"],
        price_info=simulated_show[0]["price_info"],
        status="AVAILABLE",
        booking_url=simulated_show[0]["booking_url"]
    )
    db.add(rec)

    # Send email
    try:
        email_service.send_alert(
            recipient_email=task.user_email,
            movie_name=sim_movie,
            theater_name=task.theater_name,
            city=task.city,
            target_date=task.target_date,
            platform=task.platform.upper(),
            new_shows=simulated_show
        )
        status_text = "SENT"
        err = None
    except Exception as e:
        status_text = "FAILED"
        err = str(e)

    log_entry = NotificationLog(
        task_id=task.id,
        recipient=task.user_email,
        subject=f"[SIMULATION] 🚨 BOOKING OPEN: {sim_movie} at {task.theater_name}!",
        content=f"Simulated new show: {sim_movie} at {simulated_time}",
        shows_count=1,
        status=status_text,
        error_message=err
    )
    db.add(log_entry)

    task.status_message = f"🚨 Simulated drop triggered: {simulated_time} sent to {task.user_email}"
    task.last_checked_at = datetime.utcnow()
    db.commit()

    return {
        "success": True,
        "message": f"Simulated new show alert triggered for {task.user_email}!",
        "simulated_show": simulated_show[0]
    }

@app.delete("/api/trackers/{tracker_id}")
def delete_tracker(tracker_id: int, db: Session = Depends(get_db)):
    task = db.query(AlertTask).filter(AlertTask.id == tracker_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tracker not found")
    db.delete(task)
    db.commit()
    return {"success": True, "message": f"Tracker #{tracker_id} deleted"}

# --- Shows & Theater Schedule Endpoints ---

@app.get("/api/theaters/shows")
def get_theater_shows(
    city: str = "vizag",
    theater_name: str = "",
    date: str = "",
    platform: str = "all"
):
    """
    Returns live movie shows and showtimes directly from BookMyShow or District.
    """
    target_date = date or datetime.now().strftime("%Y-%m-%d")
    plat = platform.lower().strip()
    
    if "district" in plat:
        return district_scraper.get_theater_current_shows(city, theater_name, target_date)
    elif "bms" in plat or "bookmyshow" in plat:
        return bms_scraper.get_theater_current_shows(city, theater_name, target_date)
    else:
        # Check BookMyShow first (very fast TLS cffi engine)
        bms_res = bms_scraper.get_theater_current_shows(city, theater_name, target_date)
        if bms_res.get("shows") and len(bms_res["shows"]) > 0:
            return bms_res

        # Then check District (by Zomato)
        dist_res = district_scraper.get_theater_current_shows(city, theater_name, target_date)
        if dist_res.get("shows") and len(dist_res["shows"]) > 0:
            return dist_res

        # If neither platform has shows open yet for this date:
        return {
            "city": city.title(),
            "theater_name": theater_name,
            "date": target_date,
            "platform": "District & BookMyShow",
            "is_live_data": True,
            "booking_url": bms_res.get("booking_url") or dist_res.get("booking_url") or "https://in.bookmyshow.com",
            "status_message": f"ℹ️ Shows still not released for {theater_name} on {target_date} (No ticket bookings or showtimes have opened yet).",
            "total_shows": 0,
            "shows": []
        }

@app.get("/api/trackers/{tracker_id}/shows")
def get_tracker_shows(tracker_id: int, db: Session = Depends(get_db)):
    """
    Returns all detected or current shows for a specific tracker's theater directly from BookMyShow or District.
    """
    task = db.query(AlertTask).filter(AlertTask.id == tracker_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tracker not found")

    if "district" in task.platform.lower():
        result = district_scraper.get_theater_current_shows(task.city, task.theater_name, task.target_date)
    elif "sim" in task.platform.lower():
        shows = simulator_scraper.fetch_shows(task.city, task.movie_name, task.movie_code, task.theater_name, task.venue_code, task.target_date, task.format_filter)
        result = {
            "city": task.city.title(),
            "theater_name": task.theater_name,
            "date": task.target_date,
            "platform": "Demo Simulator",
            "is_live_data": False,
            "status_message": "⚡ Simulation / Demo Mode Active",
            "total_shows": len(shows),
            "shows": shows
        }
    else:
        result = bms_scraper.get_theater_current_shows(task.city, task.theater_name, task.target_date)

    result["movie_name"] = task.movie_name
    result["tracker_id"] = task.id
    return result

# --- Discovery / Autocomplete Endpoints ---

@app.get("/api/cities")
def get_cities():
    return [
        {"id": "vizag", "name": "Visakhapatnam (Vizag)"},
        {"id": "vijayawada", "name": "Vijayawada"},
        {"id": "guntur", "name": "Guntur"},
        {"id": "tirupati", "name": "Tirupati"},
        {"id": "rajahmundry", "name": "Rajahmundry"},
        {"id": "nellore", "name": "Nellore"},
        {"id": "kurnool", "name": "Kurnool"},
        {"id": "hyderabad", "name": "Hyderabad"},
        {"id": "warangal", "name": "Warangal"},
        {"id": "karimnagar", "name": "Karimnagar"},
        {"id": "nizamabad", "name": "Nizamabad"},
        {"id": "khammam", "name": "Khammam"},
        {"id": "mahabubnagar", "name": "Mahabubnagar"}
    ]

@app.get("/api/search/movies")
def search_movies(
    city: str = "vizag",
    query: str = "",
    platform: str = "all"
):
    plat = platform.lower().strip()
    if "district" in plat:
        return district_scraper.search_movies(city, query)
    elif "sim" in plat:
        return simulator_scraper.search_movies(city, query)
    elif "bms" in plat or "bookmyshow" in plat:
        return bms_scraper.search_movies(city, query)
    else:
        # Merge both catalogs deduplicated
        d_movies = district_scraper.search_movies(city, query)
        b_movies = bms_scraper.search_movies(city, query)
        seen = set()
        merged = []
        for m in d_movies + b_movies:
            key = m["name"].lower().strip()
            if key not in seen:
                seen.add(key)
                merged.append(m)
        return merged

@app.get("/api/search/theaters")
def search_theaters(
    city: str = "vizag",
    query: str = "",
    platform: str = "all"
):
    plat = platform.lower().strip()
    if "district" in plat:
        return district_scraper.search_theaters(city, query)
    elif "sim" in plat:
        return simulator_scraper.search_theaters(city, query)
    elif "bms" in plat or "bookmyshow" in plat:
        return bms_scraper.search_theaters(city, query)
    else:
        # Return unified catalog
        d_theaters = district_scraper.search_theaters(city, query)
        b_theaters = bms_scraper.search_theaters(city, query)
        seen = set()
        merged = []
        for t in d_theaters + b_theaters:
            key = t["name"].lower().strip()
            if key not in seen:
                seen.add(key)
                merged.append(t)
        return merged

# --- Email & SMTP Endpoints ---

@app.get("/api/settings/smtp")
def get_smtp_settings():
    return {
        "is_configured": email_service.is_configured(),
        "smtp_server": settings.SMTP_SERVER,
        "smtp_port": settings.SMTP_PORT,
        "smtp_user": settings.SMTP_USER,
        "sender_email": settings.SENDER_EMAIL or settings.SMTP_USER,
        "sender_name": settings.SENDER_NAME,
        "has_password": bool(settings.SMTP_PASSWORD)
    }

@app.post("/api/settings/smtp")
def update_smtp_settings(payload: SMTPSettingsRequest):
    try:
        save_smtp_settings(
            user=payload.smtp_user,
            password=payload.smtp_password,
            server=payload.smtp_server or "smtp.gmail.com",
            port=payload.smtp_port or 587,
            sender_email=payload.sender_email or payload.smtp_user,
            sender_name=payload.sender_name or "Showzy"
        )
        return {
            "success": True,
            "message": "SMTP credentials saved and updated successfully!",
            "is_configured": email_service.is_configured()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/test-email")
def test_email(payload: TestEmailRequest):
    result = email_service.send_test_email(payload.recipient_email)
    return result

@app.get("/api/logs")
def get_logs(db: Session = Depends(get_db)):
    logs = db.query(NotificationLog).order_by(NotificationLog.sent_at.desc()).limit(30).all()
    return [
        {
            "id": l.id,
            "task_id": l.task_id,
            "recipient": l.recipient,
            "subject": l.subject,
            "content": l.content,
            "status": l.status,
            "error_message": l.error_message,
            "sent_at": l.sent_at.strftime("%Y-%m-%d %I:%M:%S %p") if l.sent_at else ""
        }
        for l in logs
    ]

# --- Live Tab Monitor & Heartbeat Endpoints ---

@app.post("/api/monitor/cycle")
async def trigger_monitor_cycle(force_all: bool = Query(False)):
    """
    Active keep-alive monitor trigger from browser tab or external webhook.
    Runs a check cycle on active trackers and returns execution stats.
    """
    try:
        result = await monitor_service.run_check_cycle(force_all=force_all)
        return {"status": "success", "result": result}
    except Exception as e:
        logger.error(f"Error in triggered monitor cycle: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/api/monitor/status")
def get_monitor_status(db: Session = Depends(get_db)):
    """
    Returns monitoring status, active tracker count, and server status.
    """
    active_count = db.query(AlertTask).filter(AlertTask.is_active == True).count()
    total_count = db.query(AlertTask).count()
    return {
        "status": "healthy",
        "is_running": monitor_service.is_running,
        "active_trackers_count": active_count,
        "total_trackers_count": total_count,
        "app_name": settings.APP_NAME,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
