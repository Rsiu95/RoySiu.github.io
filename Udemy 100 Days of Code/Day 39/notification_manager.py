import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

load_dotenv()

TWILIO_API = os.getenv("TWILIO_API")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_NUMBER = os.getenv("MY_NUMBER")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_API)
        
    def send_message(self):
        message = self.client.messages.create(
            body = f"Low price alert! only ${self.price} to fly from {self.departure_city_name}-{self.departure_city_code} to {self.arrival_city}-{self.arrival_city_code}, from {self.outbound_date} to {self.inbout_date}",
            from_ = TWILIO_NUMBER,
            to = MY_NUMBER
            
        )
        print(f"Message sent to {MY_NUMBER}\nLow price alert! only ${self.price} to fly from {self.departure_city_name}-{self.departure_city_code} to {self.arrival_city}-{self.arrival_city_code}, from {self.outbound_date} to {self.inbout_date}")