from app.config import Config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime


def send_email_verification(user_email: str, token: str):
    verify_link = f"{Config.AURELIA_REDIRECT_URI}/profileTab?token={token}"

    send_email(
        to=user_email,
        subject="Verify Your Email Address",
        title="Verify Your Email",
        body="Please verify your email address by clicking the button below. If you did not create an account, please ignore this email.",
        button_text="Verify Email",
        button_link=verify_link,
    )


def send_email_verified_notification(email: str):
    send_email(
        to=email,
        subject="Your Email Has Been Verified!",
        title="Email Verified",
        body="Your email address has been successfully verified. Thank you for confirming your email! If you did not request this, please contact support immediately.",
        button_text="Contact Support",
        button_link="mailto:contactaurelialabs@gmail.com",
    )


def send_change_email_verification(new_email: str, token: str):
    verify_link = f"{Config.AURELIA_REDIRECT_URI}/change-email?token={token}"

    send_email(
        to=new_email,
        subject="Verify Your New Email Address",
        title="Verify Your Email",
        body="Please verify your new email address by clicking the button below. If you did not request this change, please ignore this email.",
        button_text="Verify Email",
        button_link=verify_link,
    )


def send_email_change_notification(new_email: str):
    send_email(
        to=new_email,
        subject="Your Email Address Has Been Changed",
        title="Aurelia Notification",
        body="Your email address was successfully updated. If you did not make this change, please contact support immediately.",
        button_text="Contact Support",
        button_link="mailto:contactaurelialabs@gmail.com",
    )


def send_password_change_notification(user_email: str):
    send_email(
        to=user_email,
        subject="Your Password Has Been Changed",
        title="Aurelia Notification",
        body="Your password was successfully updated. If you did not make this change, please contact support immediately.",
        button_text="Contact Support",
        button_link="mailto:contactaurelialabs@gmail.com",
    )


def send_password_reset_email(userEmail: str, reset_token: str):
    reset_link = f"{Config.AURELIA_REDIRECT_URI}/reset-password?token={reset_token}"

    send_email(
        to=userEmail,
        subject="Reset Your Password",
        title="Reset Your Password",
        body="You requested a password reset. Click the button below to reset your password. This link will expire in 30 minutes.",
        button_text="Reset Password",
        button_link=reset_link,
    )


def send_email(
    to: str,
    subject: str,
    title: str,
    body: str,
    button_text: str,
    button_link: str,
):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = Config.EMAIL_USER
    sender_password = Config.EMAIL_PASS

    html_body = f"""
    <html>
      <body style="background: #f5f7ff; font-family: Arial, sans-serif; padding: 24px;">
        <div style="max-width: 600px; margin: 40px auto; background: #fff; border-radius: 10px; box-shadow: 0 2px 12px #e0e0e0; padding: 40px; text-align: center;">
          <h2 style="color: #81c6d0; margin-top: 0;">{title}</h2>
          <div style="font-size: 16px; color: #222; margin-bottom: 32px;">
            {body}
          </div>
          <a href="{button_link}" style="display: inline-block; padding: 12px 28px; background: #81c6d0; color: #fff; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 16px;">
            {button_text}
          </a>
        </div>
        <div style="max-width: 600px; margin: 0 auto; text-align: center;">
          <footer style="font-size: 12px; color: #888;      margin-top: 32px;">
           &copy; {datetime.now().year} Aurelia Labs. All rights reserved.<br>
           Aurelia™ is a trademark of Aurelia Labs.
          </footer>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["From"] = f'Aurelia Labs <{sender_email}>'
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, msg.as_string())
        server.quit()
        print(f"Email sent to {to}")
    except Exception as e:
        print(f"Failed to send email: {e}")
