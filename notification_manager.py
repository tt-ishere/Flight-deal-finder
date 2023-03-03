from twilio.rest import Client
from environment_variables import account_sid, auth_token, PASSWORD
import smtplib

SENDER = "enoch260@gmail.com"


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, sms):
        message = self.client.messages.create(
            body=sms,
            from_="+17407167716",
            to="+233268125555",
        )
        print(message.sid)

    def send_email(self, message, emails, deep_link):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=SENDER,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight deal!\n\n{message}\n{deep_link}".encode(
                        "utf-8"
                    ),
                )
                print("Message sent")
