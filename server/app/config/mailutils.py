from flask_mail import Message
from app import mail
import threading
from flask import current_app


def send_mail(to_email: str, name: str, otp: str, subject: str):

    msg = Message(
        subject=subject,
        sender="ansariali.developer@gmail.com",
        recipients=[to_email],
    )

    msg.html = f"""
    <div style="font-family:sans-serif;max-width:480px;margin:auto;padding:32px;
                border:1px solid #e5e7eb;border-radius:16px;">
      <h2 style="color:#7c3aed;margin-bottom:4px;">Eduvia</h2>
      <p style="color:#6b7280;font-size:14px;margin-top:0;">AI-Powered Study Planner</p>
      <hr style="margin:24px 0;">
      <p>Hi <strong>{name}</strong>,</p>
      <p>{subject}</p>
      <div style="text-align:center;margin:32px 0;">
        <h1>{otp}</h1>
      </div>
      <p style="text-align:center;font-size:12px;">
        OTP valid for 10 minutes
      </p>
    </div>
    """

    app = current_app._get_current_object()

    def send():
        with app.app_context():
            mail.send(msg)

    threading.Thread(target=send).start()