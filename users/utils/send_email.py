from email.mime.text import MIMEText
import smtplib
from fastapi import HTTPException
from core.settings import SMTP_USERNAME, SMTP_PASSWORD


async def send_email(to: str, subject: str, body: str):

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = SMTP_USERNAME
    smtp_password = SMTP_PASSWORD

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = smtp_username
    msg["To"] = to

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, [to], msg.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
