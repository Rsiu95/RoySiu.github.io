import requests
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):       
        self.SHEETY_API = os.getenv("SHEETY_API")
        self.SHEETY_AUTH = os.getenv("SHEETY_AUTH")
        self.SHEETY_PATH = f"https://api.sheety.co/{self.SHEETY_API}/flightDeals/prices"
        self.sheety_headers = {
            "Authorization": f"Basic {self.SHEETY_AUTH}"
        }
        self.response = requests.get(url = self.SHEETY_PATH, headers = self.sheety_headers)
        self.response.raise_for_status()
        self.prices = self.response.json()
        
    def update_sheet(self, prices, id):
        self.response = requests.put(url = self.SHEETY_PATH + f"/{id}", headers = self.sheety_headers, json = prices)
        self.response.raise_for_status()
