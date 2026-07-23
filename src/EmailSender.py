from Email import Email
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

class EmailSender:
    sender_email: str
    email_password: str

    def __init__(self, sender_email: str, email_password: str) -> None:
        self.sender_email = sender_email
        self.email_password = email_password

    def send_email(self, email: Email) -> bool:
        msg = MIMEText(email.body, "html")
        msg["Subject"] = email.subject
        msg["From"] = email.sender
        msg["To"] = email.receiver

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(email.sender, self.email_password)
                server.sendmail(email.sender, email.receiver, msg.as_string())
                return True
        except smtplib.SMTPException as e:
            print(f"Error: unable to send email: {e}")
        return False