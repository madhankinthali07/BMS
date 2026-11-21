import asyncio
import logging
from datetime import datetime
from typing import List, Dict, Any
from database import SessionLocal
from models import AlertTask, ShowRecord, NotificationLog
from scrapers import get_scraper_for_platform, bms_scraper, district_scraper, simulator_scraper
from notifiers.email_service import email_service

logger = logging.getLogger(__name__)

class MonitorService:
    """
    Background scheduler and state diffing engine for live show monitoring.
    """

    def __init__(self):
        self.is_running = False
        self._task = None

    async def start(self):
        if self.is_running:
            return
        self.is_running = True
        self._task = asyncio.create_task(self._monitor_loop())
        logger.info("MonitorService started in background.")

    async def stop(self):
        self.is_running = False
        if self._task and not self._task.done():
            self._task.cancel()
            try:
                await self._task
            except (asyncio.CancelledError, Exception):
                pass
        logger.info("MonitorService stopped.")

    async def _monitor_loop(self):
        while self.is_running:
            try:
                await self.run_check_cycle()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in monitor check cycle: {e}", exc_info=True)
            
            try:
                await asyncio.sleep(10)
            except asyncio.CancelledError:
                break

    async def run_check_cycle(self, force_all: bool = False):
        """
        Polls active alert tasks that are due for checking.
        Runs blocking DB and scraper work in worker threads to keep event loop responsive.
        """
        return await asyncio.to_thread(self._sync_check_cycle, force_all)

    def _sync_check_cycle(self, force_all: bool = False):
        db = SessionLocal()
        checked_count = 0
        new_shows_found = 0
        try:
            now = datetime.utcnow()
            active_tasks = db.query(AlertTask).filter(AlertTask.is_active == True).all()

            for task in active_tasks:
                should_check = force_all
                if not should_check:
                    if not task.last_checked_at:
                        should_check = True
                    else:
                        elapsed = (now - task.last_checked_at).total_seconds()
                        if elapsed >= task.check_interval:
                            should_check = True

                if should_check:
                    res = self._process_task_sync(db, task)
                    checked_count += 1
                    new_shows_found += res.get("new_shows_count", 0)

            return {
                "active_tasks": len(active_tasks),
                "checked_tasks": checked_count,
                "new_shows_found": new_shows_found,
                "timestamp": now.strftime("%I:%M:%S %p")
            }
        finally:
            db.close()

    async def check_task_now(self, task_id: int) -> Dict[str, Any]:
        """
        Immediately check a specific task on user demand.
        """
        return await asyncio.to_thread(self._sync_check_task_now, task_id)

    def _sync_check_task_now(self, task_id: int) -> Dict[str, Any]:
        db = SessionLocal()
        try:
            task = db.query(AlertTask).filter(AlertTask.id == task_id).first()
            if not task:
                return {"success": False, "message": "Tracker not found"}
            return self._process_task_sync(db, task)
        finally:
            db.close()

    def _process_task_sync(self, db, task: AlertTask) -> Dict[str, Any]:
        """
        Performs scrape, diff calculation, state update, and email notification synchronously in thread.
        """
        task_id = task.id
        now_str = datetime.now().strftime("%I:%M:%S %p")
        logger.info(f"Checking Task #{task_id}: {task.movie_name} at {task.theater_name} ({task.platform})")

        # 1. Fetch current live shows from scrapers
        fetched_shows: List[Dict[str, Any]] = []
        platform_lower = task.platform.lower()

        try:
            if "both" in platform_lower:
                bms_res = bms_scraper.fetch_shows(
                    city=task.city,
                    movie_name=task.movie_name,
                    movie_code=task.movie_code,
                    theater_name=task.theater_name,
                    venue_code=task.venue_code,
                    target_date=task.target_date,
                    format_filter=task.format_filter
                )
                dist_res = district_scraper.fetch_shows(
                    city=task.city,
                    movie_name=task.movie_name,
                    movie_code=task.movie_code,
                    theater_name=task.theater_name,
                    venue_code=task.venue_code,
                    target_date=task.target_date,
                    format_filter=task.format_filter
                )
                fetched_shows = bms_res + dist_res
            elif "district" in platform_lower:
                fetched_shows = district_scraper.fetch_shows(
                    city=task.city,
                    movie_name=task.movie_name,
                    movie_code=task.movie_code,
                    theater_name=task.theater_name,
                    venue_code=task.venue_code,
                    target_date=task.target_date,
                    format_filter=task.format_filter
                )
            elif "sim" in platform_lower:
                fetched_shows = simulator_scraper.fetch_shows(
                    city=task.city,
                    movie_name=task.movie_name,
                    movie_code=task.movie_code,
                    theater_name=task.theater_name,
                    venue_code=task.venue_code,
                    target_date=task.target_date,
                    format_filter=task.format_filter
                )
            else:
                fetched_shows = bms_scraper.fetch_shows(
                    city=task.city,
                    movie_name=task.movie_name,
                    movie_code=task.movie_code,
                    theater_name=task.theater_name,
                    venue_code=task.venue_code,
                    target_date=task.target_date,
                    format_filter=task.format_filter
                )
        except Exception as e:
            logger.error(f"Error fetching shows for task #{task_id}: {e}")
            task.status_message = f"Check failed at {now_str}: {str(e)[:100]}"
            task.last_checked_at = datetime.utcnow()
            db.commit()
            return {"success": False, "message": str(e), "new_shows": 0}

        # 2. Diff calculation against existing saved shows for this task
        existing_show_ids = {
            s.show_id for s in db.query(ShowRecord).filter(ShowRecord.task_id == task_id).all()
        }

        newly_detected_shows = []
        for s in fetched_shows:
            s_id = s.get("show_id")
            if s_id not in existing_show_ids:
                newly_detected_shows.append(s)

        # 3. Handle newly found shows
        if newly_detected_shows:
            logger.info(f"🚨 [SHOW ALERT] Task #{task_id}: Found {len(newly_detected_shows)} new showtimes!")

            # Determine movie name(s) to alert
            m_upper = (task.movie_name or "").strip().upper()
            is_any_movie = (
                not m_upper or 
                m_upper in ["ALL", "ANY", "*", "ALL MOVIES", "ANY MOVIE"] or 
                "ANY MOVIE" in m_upper or 
                "ALL MOVIES" in m_upper
            )
            detected_movie_titles = sorted(list({s.get("movie_name") for s in newly_detected_shows if s.get("movie_name")}))
            if is_any_movie and detected_movie_titles:
                alert_movie_name = ", ".join(detected_movie_titles)
            else:
                alert_movie_name = task.movie_name
            
            # Save new shows to database
            for s in newly_detected_shows:
                show_rec = ShowRecord(
                    task_id=task_id,
                    show_id=s.get("show_id"),
                    platform=s.get("platform", task.platform),
                    show_time=s.get("show_time", ""),
                    format_type=s.get("format_type", "2D"),
                    price_info=s.get("price_info", ""),
                    status=s.get("status", "AVAILABLE"),
                    booking_url=s.get("booking_url", "")
                )
                db.add(show_rec)

            # Trigger email notification
            email_status = "SENT"
            error_msg = None
            try:
                email_service.send_alert(
                    recipient_email=task.user_email,
                    movie_name=alert_movie_name,
                    theater_name=task.theater_name,
                    city=task.city,
                    target_date=task.target_date,
                    platform=task.platform.upper(),
                    new_shows=newly_detected_shows
                )
            except Exception as mail_err:
                email_status = "FAILED"
                error_msg = str(mail_err)
                logger.error(f"Failed to dispatch email for task #{task_id}: {mail_err}")

            # Record notification log
            notif_log = NotificationLog(
                task_id=task_id,
                recipient=task.user_email,
                subject=f"🚨 BOOKING OPEN: {alert_movie_name} at {task.theater_name}!",
                content=f"Sent alert for {len(newly_detected_shows)} new shows ({alert_movie_name}).",
                shows_count=len(newly_detected_shows),
                status=email_status,
                error_message=error_msg
            )
            db.add(notif_log)

            task.status_message = f"🚨 {len(newly_detected_shows)} shows detected for {alert_movie_name}! Email sent at {now_str}"
        else:
            task.status_message = f"Checked at {now_str} - {len(fetched_shows)} active shows (no new added)"

        task.last_checked_at = datetime.utcnow()
        task.last_shows_count = len(fetched_shows)
        db.commit()

        return {
            "success": True,
            "message": task.status_message,
            "new_shows_count": len(newly_detected_shows),
            "total_shows_count": len(fetched_shows)
        }

monitor_service = MonitorService()
