import requests
from dotenv import load_dotenv
import os

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        self.KIWI_API = os.getenv("KIWI_API")
        self.KIWI_PATH = f"https://api.tequila.kiwi.com/locations/query"
        self.KIWI_HEADERS = {
            "apikey": self.KIWI_API,
        }
        self.KIWI_PARAMS = {
            "term": city,
            "location_types": "airport",
        }
        
        response = requests.get(url = self.KIWI_PATH, headers = self.KIWI_HEADERS, params = self.KIWI_PARAMS)
        response.raise_for_status()
        data = response.json()
        for id in data['locations']:
            return id['id']
