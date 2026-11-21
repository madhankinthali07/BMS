import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Showzy - BMS & District Show Tracker"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")
    
    # Database
    DATABASE_URL: str = "sqlite:///./cinealert.db"
    
    # Email / SMTP Configuration
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    SENDER_EMAIL: str = os.getenv("SENDER_EMAIL", "")
    SENDER_NAME: str = os.getenv("SENDER_NAME", "Showzy")
    
    # Default Monitoring Interval (in seconds)
    DEFAULT_CHECK_INTERVAL: int = 120  # Every 2 minutes
    MIN_CHECK_INTERVAL: int = 30       # Minimum allowed to prevent IP rate-limiting
    
    # Scraper Headers
    DEFAULT_USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

def save_smtp_settings(user: str, password: str, server: str = "smtp.gmail.com", port: int = 587, sender_email: str = "", sender_name: str = "Showzy"):
    """
    Updates in-memory settings and persists them into the .env file.
    """
    settings.SMTP_USER = user.strip()
    settings.SMTP_PASSWORD = password.strip().replace(" ", "")  # Google App Passwords often have spaces
    settings.SMTP_SERVER = server.strip()
    settings.SMTP_PORT = port
    settings.SENDER_EMAIL = sender_email.strip() or user.strip()
    settings.SENDER_NAME = sender_name.strip()

    # Update or create .env file
    env_content = f"""# CineAlert Configuration File
HOST={settings.HOST}
PORT={settings.PORT}
DEBUG={settings.DEBUG}
DATABASE_URL={settings.DATABASE_URL}

# Email / SMTP Settings
SMTP_SERVER={settings.SMTP_SERVER}
SMTP_PORT={settings.SMTP_PORT}
SMTP_USER={settings.SMTP_USER}
SMTP_PASSWORD={settings.SMTP_PASSWORD}
SENDER_EMAIL={settings.SENDER_EMAIL}
SENDER_NAME={settings.SENDER_NAME}

DEFAULT_CHECK_INTERVAL={settings.DEFAULT_CHECK_INTERVAL}
MIN_CHECK_INTERVAL={settings.MIN_CHECK_INTERVAL}
"""
    with open(".env", "w", encoding="utf-8") as f:
        f.write(env_content)
