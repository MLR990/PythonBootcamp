import smtplib

from twilio.rest import Client

TWILIO_SID = "TWILIO_ACCOUNT_ID"
TWILIO_AUTH_TOKEN = "TWILIO_TOKEN"

TWILIO_VIRTUAL_NUMBER = "VIRTUAL_NUMBER"
TWILIO_VERIFIED_NUMBER = "VERIFIED_NUMBER"

MY_EMAIL = "michaellreagan@gmail.com"
MY_PASSWORD = "gmailPassword"
EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
