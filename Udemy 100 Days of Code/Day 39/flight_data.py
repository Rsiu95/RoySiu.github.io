import requests
from dotenv import load_dotenv
import os
import datetime as dt
load_dotenv()



class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport_code, departure_city):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        
    def search_flights(self, departure_date, return_date):
        tomorrow = dt.datetime.now() + dt.timedelta(days = 1)
        departure_range = tomorrow + dt.timedelta(days = 182.5)
        # TODO looking for round trips that return between 7 and 28 days in length > return_from
        
        return_earliest = ""
        return_latest = ""

        KIWI_API = os.getenv("KIWI_API")
        KIWI_PATH = f"https://api.tequila.kiwi.com/v2/search"
        KIWI_HEADERS = {
            "apikey": KIWI_API,
        }
        KIWI_PARAMS = {
            "fly_from": self.departure_airport_code,
            "date_from": departure_date,
            "date_to": departure_range.strftime("%d/%m/%Y"),
            "return_from": return_date,
            "return_to": "",
            "max_stopovers": 0,
            "curr": "AUD"
            
            
        }
        response = requests.get(url = KIWI_PATH, headers = KIWI_HEADERS, params = KIWI_PARAMS)