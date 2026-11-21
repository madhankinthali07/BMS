from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel, field_validator
from typing import Optional, List

# --- SQLAlchemy Models ---

class AlertTask(Base):
    __tablename__ = "alert_tasks"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(50), default="bookmyshow")  # "bookmyshow", "district", "both"
    city = Column(String(100), nullable=False)
    movie_name = Column(String(200), nullable=False)
    movie_code = Column(String(100), nullable=True)      # BMS event code or District slug/id
    theater_name = Column(String(200), nullable=False)
    venue_code = Column(String(100), nullable=True)      # BMS venue code or District venue id
    target_date = Column(String(20), nullable=False)      # YYYY-MM-DD or YYYYMMDD
    format_filter = Column(String(100), default="ALL")    # "ALL", "IMAX", "4DX", "3D", "2D", etc.
    user_email = Column(String(150), nullable=False)
    
    is_active = Column(Boolean, default=True)
    check_interval = Column(Integer, default=120)         # Seconds
    last_checked_at = Column(DateTime, nullable=True)
    last_shows_count = Column(Integer, default=0)
    status_message = Column(String(300), default="Initialized")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    shows = relationship("ShowRecord", back_populates="task", cascade="all, delete-orphan")
    notifications = relationship("NotificationLog", back_populates="task", cascade="all, delete-orphan")


class ShowRecord(Base):
    __tablename__ = "show_records"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("alert_tasks.id"))
    show_id = Column(String(150), index=True)             # Unique identifier for the show instance
    platform = Column(String(50), default="bookmyshow")
    show_time = Column(String(50), nullable=False)        # E.g. "10:30 AM", "07:15 PM"
    format_type = Column(String(50), default="2D")        # E.g. "IMAX 2D", "3D", "4DX"
    price_info = Column(String(100), nullable=True)
    status = Column(String(50), default="AVAILABLE")      # "AVAILABLE", "FILLING_FAST", "SOLD_OUT"
    booking_url = Column(Text, nullable=True)
    detected_at = Column(DateTime, default=datetime.utcnow)

    task = relationship("AlertTask", back_populates="shows")


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("alert_tasks.id"), nullable=True)
    recipient = Column(String(150), nullable=False)
    subject = Column(String(300), nullable=False)
    content = Column(Text, nullable=False)
    shows_count = Column(Integer, default=1)
    status = Column(String(50), default="SENT")           # "SENT", "FAILED", "TEST"
    error_message = Column(Text, nullable=True)
    sent_at = Column(DateTime, default=datetime.utcnow)

    task = relationship("AlertTask", back_populates="notifications")


# --- Pydantic Schemas ---

class TrackerCreateRequest(BaseModel):
    platform: str = "bookmyshow"                          # "bookmyshow", "district", "both", "simulation"
    city: str
    movie_name: str
    movie_code: Optional[str] = ""
    theater_name: str
    venue_code: Optional[str] = ""
    target_date: str                                      # YYYY-MM-DD
    format_filter: Optional[str] = "ALL"
    user_email: str
    check_interval: Optional[int] = 120

    @field_validator("user_email")
    def validate_email_format(cls, v):
        v = v.strip()
        if "@" not in v or "." not in v:
            raise ValueError("Invalid email address format")
        return v

class TrackerResponse(BaseModel):
    id: int
    platform: str
    city: str
    movie_name: str
    movie_code: Optional[str]
    theater_name: str
    venue_code: Optional[str]
    target_date: str
    format_filter: str
    user_email: str
    is_active: bool
    check_interval: int
    last_checked_at: Optional[datetime]
    last_shows_count: int
    status_message: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class ShowItem(BaseModel):
    show_id: str
    platform: str
    theater_name: str
    movie_name: str
    show_time: str
    format_type: str
    price_info: Optional[str] = ""
    status: str
    booking_url: Optional[str] = ""

class TestEmailRequest(BaseModel):
    recipient_email: str

    @field_validator("recipient_email")
    def validate_email_format(cls, v):
        v = v.strip()
        if "@" not in v or "." not in v:
            raise ValueError("Invalid email address format")
        return v

class SMTPSettingsRequest(BaseModel):
    smtp_user: Optional[str] = ""
    smtp_password: Optional[str] = ""
    smtp_server: Optional[str] = "smtp.gmail.com"
    smtp_port: Optional[int] = 587
    sender_email: Optional[str] = ""
    sender_name: Optional[str] = "Showzy"
    resend_api_key: Optional[str] = ""
