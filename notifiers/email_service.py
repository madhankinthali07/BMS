import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Any, Optional
from config import settings

logger = logging.getLogger(__name__)

class EmailNotifier:
    """
    Service responsible for building and dispatching instant movie ticket email alerts.
    Directly references live settings so updates from the dashboard take effect immediately.
    """

    @property
    def smtp_server(self) -> str:
        return settings.SMTP_SERVER or "smtp.gmail.com"

    @property
    def smtp_port(self) -> int:
        return settings.SMTP_PORT or 587

    @property
    def smtp_user(self) -> str:
        return settings.SMTP_USER.strip()

    @property
    def smtp_password(self) -> str:
        # Strip spaces because users often paste Google App Passwords like 'abcd efgh ijkl mnop'
        return settings.SMTP_PASSWORD.replace(" ", "").strip()

    @property
    def sender_email(self) -> str:
        return (settings.SENDER_EMAIL or settings.SMTP_USER).strip()

    @property
    def sender_name(self) -> str:
        return settings.SENDER_NAME or "Showzy"

    def is_configured(self) -> bool:
        return bool(self.smtp_user and self.smtp_password and self.sender_email)

    def _build_html_body(
        self,
        movie_name: str,
        theater_name: str,
        city: str,
        target_date: str,
        platform: str,
        new_shows: List[Dict[str, Any]]
    ) -> str:
        shows_html = ""
        for s in new_shows:
            booking_url = s.get("booking_url") or "https://in.bookmyshow.com"
            s_movie = s.get("movie_name") or movie_name
            shows_html += f"""
            <tr style="border-bottom: 1px solid #2d3748;">
                <td style="padding: 14px 12px; font-weight: bold; font-size: 16px; color: #ffffff;">
                    {s.get('show_time')}
                </td>
                <td style="padding: 14px 12px;">
                    <span style="background: #9565F5; color: #ffffff; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 600; text-transform: uppercase;">
                        {s.get('format_type', '2D')}
                    </span>
                </td>
                <td style="padding: 14px 12px; color: #F5F2FA; font-size: 14px; font-weight: 500;">
                    {s_movie}
                </td>
                <td style="padding: 14px 12px; text-align: right;">
                    <a href="{booking_url}" target="_blank" style="background: #9565F5; color: #ffffff; text-decoration: none; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: bold; display: inline-block;">
                        Book Now &rarr;
                    </a>
                </td>
            </tr>
            """

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Movie Shows Alert!</title>
        </head>
        <body style="margin: 0; padding: 0; background-color: #0f172a; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #f8fafc;">
            <div style="max-width: 620px; margin: 30px auto; background-color: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.5); border: 1px solid #334155;">
                
                <!-- Header Banner -->
                <div style="background: linear-gradient(135deg, #e50914 0%, #b81d24 100%); padding: 28px 24px; text-align: center;">
                    <h1 style="margin: 0; font-size: 24px; color: #ffffff; letter-spacing: 0.5px;">
                        🚨 SHOWS OPENED!
                    </h1>
                    <p style="margin: 6px 0 0 0; color: #ffe4e6; font-size: 14px;">
                        Instant Ticket Alert from {settings.APP_NAME}
                    </p>
                </div>

                <!-- Movie & Venue Card -->
                <div style="padding: 24px 24px 10px 24px;">
                    <div style="background-color: #0f172a; border-radius: 8px; padding: 18px; border-left: 4px solid #e50914;">
                        <h2 style="margin: 0 0 8px 0; font-size: 20px; color: #f8fafc;">
                            🎬 {movie_name}
                        </h2>
                        <div style="color: #94a3b8; font-size: 14px; line-height: 1.6;">
                            <div><strong>🏛 Theater:</strong> {theater_name}</div>
                            <div><strong>📍 City:</strong> {city.title()}</div>
                            <div><strong>📅 Date:</strong> {target_date}</div>
                            <div><strong>🎟 Platform:</strong> {platform}</div>
                        </div>
                    </div>
                </div>

                <!-- Showtimes Table -->
                <div style="padding: 10px 24px 24px 24px;">
                    <h3 style="margin: 16px 0 12px 0; font-size: 16px; color: #cbd5e1; text-transform: uppercase; letter-spacing: 0.5px;">
                        New Detected Shows ({len(new_shows)})
                    </h3>
                    <table style="width: 100%; border-collapse: collapse; text-align: left;">
                        <thead>
                            <tr style="border-bottom: 2px solid #334155; color: #94a3b8; font-size: 12px; text-transform: uppercase;">
                                <th style="padding: 8px 12px;">Timing</th>
                                <th style="padding: 8px 12px;">Format</th>
                                <th style="padding: 8px 12px;">Movie</th>
                                <th style="padding: 8px 12px; text-align: right;">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            {shows_html}
                        </tbody>
                    </table>
                </div>

                <!-- Footer -->
                <div style="background-color: #0f172a; padding: 16px 24px; text-align: center; border-top: 1px solid #334155;">
                    <p style="margin: 0; color: #64748b; font-size: 12px;">
                        Tickets on popular platforms sell out in minutes! Click the link above to secure your seats immediately.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        return html

    def send_alert(
        self,
        recipient_email: str,
        movie_name: str,
        theater_name: str,
        city: str,
        target_date: str,
        platform: str,
        new_shows: List[Dict[str, Any]]
    ) -> bool:
        """
        Sends showtime alert email to the user.
        Raises an informative Exception if SMTP is not configured or fails.
        """
        recipient_email = recipient_email.strip()
        if not recipient_email:
            raise ValueError("Recipient email is empty")

        if not self.is_configured():
            msg = (
                f"Email alert could not be sent to '{recipient_email}' because Gmail SMTP is not configured. "
                f"Please open the 'Email & SMTP Setup' tab in the app and enter your Gmail address and 16-character Google App Password."
            )
            logger.warning(msg)
            print(f"\n⚠️  {msg}\n")
            raise RuntimeError(msg)

        subject = f"🚨 BOOKING OPEN: {movie_name} at {theater_name} ({platform})!"
        
        html_content = self._build_html_body(
            movie_name=movie_name,
            theater_name=theater_name,
            city=city,
            target_date=target_date,
            platform=platform,
            new_shows=new_shows
        )

        plain_text = (
            f"SHOWS OPENED!\n\n"
            f"Movie: {movie_name}\n"
            f"Theater: {theater_name} ({city})\n"
            f"Date: {target_date}\n"
            f"Platform: {platform}\n\n"
            f"Shows:\n"
        )
        for s in new_shows:
            plain_text += f"- {s.get('show_time')} | {s.get('format_type')} | {s.get('price_info')} -> {s.get('booking_url')}\n"

        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = f"{self.sender_name} <{self.sender_email}>"
            msg["To"] = recipient_email

            msg.attach(MIMEText(plain_text, "plain"))
            msg.attach(MIMEText(html_content, "html"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=12) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())

            logger.info(f"Show alert email sent successfully to {recipient_email}")
            return True

        except smtplib.SMTPAuthenticationError as e:
            err_msg = (
                f"Gmail rejected your login credentials: {e}. "
                "Ensure that 2-Step Verification is enabled on your Google Account, "
                "and generate a 16-character App Password at https://myaccount.google.com/apppasswords "
                "(use the 16-character app password, not your personal Gmail login password)."
            )
            logger.error(err_msg)
            raise RuntimeError(err_msg)

        except Exception as e:
            err_msg = f"Failed to deliver email via {self.smtp_server}:{self.smtp_port}: {str(e)}"
            logger.error(err_msg)
            raise RuntimeError(err_msg)

    def send_test_email(self, recipient_email: str) -> Dict[str, Any]:
        """
        Sends a test verification email and returns structured status and message.
        """
        test_shows = [{
            "show_time": "06:30 PM (Prime Show)",
            "format_type": "4K Dolby Atmos",
            "price_info": "₹200 - ₹350",
            "booking_url": "https://in.bookmyshow.com"
        }]
        
        try:
            self.send_alert(
                recipient_email=recipient_email,
                movie_name="Verified Test Movie",
                theater_name="Jagadamba 70mm Multiplex",
                city="Visakhapatnam (Vizag)",
                target_date="Today",
                platform="BookMyShow & District",
                new_shows=test_shows
            )
            return {
                "success": True,
                "message": f"Success! Verification email delivered to '{recipient_email}'. Check your inbox (or spam folder)!"
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

email_service = EmailNotifier()
