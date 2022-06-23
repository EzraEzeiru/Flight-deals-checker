from twilio.rest import Client
TWILIO_SID = 'AC435360369294021f4ab2b76872cd46cf'
TWILIO_AUTH_TOKEN = '21d3dc5d756955ef479bc0d3dd3dc7e1'
TWILIO_VIRTUAL_NUMBER = "+19896468028"
TWILIO_VERIFIED_NUMBER = "+2349098828475"
class NotificationManager:
    def __init__(self):
       pass
    def send_sms(self, send_message):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=f"{send_message}",
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.status)
