import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


class EmailService:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.deltaglobalbank.com.br")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.smtp_user = os.getenv("SMTP_USERNAME")
        self.smtp_pass = os.getenv("SMTP_PASSWORD")
        self.from_email = os.getenv("FROM_EMAIL")

    def send_email(self, email_entity):
        headers = [
            f"From: {self.from_email}",
            f"To: {email_entity.to_email}",
            f"Subject: {email_entity.subject}",
            "MIME-Version: 1.0",
            "Content-Type: text/html; charset=utf-8",
        ]

        if email_entity.cc:
            headers.append(f"Cc: {', '.join(email_entity.cc)}")

        headers.append("")
        message = "\r\n".join(headers) + "\r\n" + email_entity.body

        all_recipients = [email_entity.to_email] + email_entity.cc + email_entity.bcc

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_pass)
                server.sendmail(self.from_email, all_recipients, message.encode("utf-8"))
            return True
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
            return False

    def check_login(self):
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=10) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_pass)
            return True
        except Exception as e:
            print(f"Erro no login SMTP: {e}")
            return False

    def check_status(self):
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=5) as server:
                server.noop()  # comando SMTP para "ping"
            return True
        except Exception as e:
            print(f"Servidor SMTP inacessível: {e}")
            return False
