# 🎬 CineAlert: BookMyShow & District Live Show Monitor

A real-time showtime monitoring and notification application for **BookMyShow** and **District (by Zomato)**. 

When a movie ticket booking window opens or new showtimes are added for your chosen movie and theater, CineAlert instantly detects the change and dispatches a rich HTML notification directly to your email address with direct booking links.

---

## ✨ Key Features

1. **Multi-Platform Support**:
   - 🎟️ **BookMyShow**: Monitors movie shows, theater schedules, and screen formats.
   - ⚡ **District (by Zomato)**: Monitors District's movie listings and live venue availability.
   - 🔄 **Both Platforms Simultaneously**: Track whether tickets drop first on BMS or District.
2. **Real-Time Diff & State Engine**:
   - Background worker service polls show data at configurable intervals (e.g. every 30s to 5 mins).
   - Intelligently detects:
     - First-time booking opens ("Available Soon" &rarr; "Booking Open").
     - Brand new show additions (e.g., late-night shows, IMAX slot drops).
     - Status updates (e.g., Sold Out &rarr; Available).
   - Prevents repetitive spam alerts by caching already notified showtimes in SQLite.
3. **Instant Email Alerts**:
   - Rich dark-mode HTML email template displaying:
     - Movie title, poster, city, and theater name.
     - Formats (IMAX 2D/3D, 4DX, Dolby Atmos, 2D).
     - Exact timings and price tiers.
     - Direct "Book Now" CTA buttons for immediate checkout.
   - Works with **Gmail (Free App Password)**, Outlook, or any custom SMTP provider.
4. **Interactive Dashboard**:
   - Dark cinema UI inspired by Netflix/BookMyShow.
   - Quick search and autocomplete for major Indian cities, theaters, and upcoming blockbusters.
   - Live Tracker Cards with check countdowns, pause/resume toggles, and deletion.
   - Built-in **"Test Alert" / Simulation Mode** to verify email delivery in seconds.
   - Detailed delivery and audit log history.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+ installed
- Windows, macOS, or Linux

### 2. Launch the Application

Double-click `run.bat` (on Windows) or run in your terminal:

```bash
# Optional: install dependencies if not already present
pip install -r requirements.txt

# Start the application
python main.py
```

Open your browser at:
👉 **`http://127.0.0.1:8000`**

---

## 📧 Setting Up Real Email Alerts (Gmail Guide)

To receive real emails on your phone or inbox, configure Gmail SMTP:

1. Go to your [Google Account](https://myaccount.google.com/) &rarr; **Security**.
2. Ensure **2-Step Verification** is turned ON.
3. In the search bar at the top of your Google Account, search for **App Passwords**.
4. Create a new App Password:
   - App Name: `CineAlert`
   - Click **Create** &rarr; copy the 16-character password generated.
5. In your project directory, copy `.env.example` to `.env`:
   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your_email@gmail.com
   SMTP_PASSWORD=your_16_character_app_password
   SENDER_EMAIL=your_email@gmail.com
   ```
6. Open the **Email & SMTP Setup** tab in the CineAlert dashboard and click **"Send Sample Show Alert Email"** to verify!

> *Note: If SMTP is not yet configured, CineAlert runs in **Simulation Mode** — all alerts are recorded in the Web Dashboard and logged to your terminal so you can test immediately without credentials.*

---

## 🛠️ Architecture Overview

```
┌────────────────────────────────────────────────────────┐
│                   Web Dashboard UI                     │
│    (Tailwind CSS + Fast HTML5 Dashboard + REST API)    │
└──────────────────────────▲─────────────────────────────┘
                           │
┌──────────────────────────┴─────────────────────────────┐
│                    FastAPI Backend                     │
│  - REST Endpoints (/api/trackers, /api/logs, etc.)     │
│  - SQLite Database (AlertTasks, ShowRecords, Logs)     │
└──────────────────────────▲─────────────────────────────┘
                           │
┌──────────────────────────┴─────────────────────────────┐
│               Background Monitor Engine                │
│  - Async Poller (Runs every X seconds)                 │
│  - State Diffing: Detects newly opened / added shows   │
└────────────┬─────────────────────────────┬─────────────┘
             │                             │
    ┌────────▼────────┐           ┌────────▼────────┐
    │ Scraper Engines │           │  Email Notifier │
    │ - BookMyShow    │           │  - HTML Email   │
    │ - District      │           │  - SMTP Client  │
    │ - Simulator     │           │  - Anti-Spam    │
    └─────────────────┘           └─────────────────┘
```

---

## 📁 Project Structure

```
c:\Users\Asus\Desktop\BMS\
├── main.py                 # FastAPI application and routing
├── config.py               # Settings and environment variables
├── database.py             # SQLite connection and session management
├── models.py               # Database schemas and Pydantic validation
├── monitor.py              # Background polling and show diffing service
├── scrapers/
│   ├── base.py             # Abstract scraper interface
│   ├── bookmyshow.py       # BookMyShow endpoints and web parser
│   ├── district.py         # District by Zomato scraper
│   └── simulator.py        # Demo engine for instant testing
├── notifiers/
│   └── email_service.py    # Responsive HTML email builder & SMTP dispatcher
├── templates/
│   └── index.html          # Modern dashboard web UI
├── .env.example            # Environment variables template
├── requirements.txt        # Python package dependencies
├── run.bat                 # Windows one-click start script
└── README.md               # Documentation
```
