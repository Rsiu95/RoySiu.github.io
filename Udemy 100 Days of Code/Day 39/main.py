#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
import datetime as dt

sheet_data = DataManager()

DEPARTURE_CITY_CODE = "MEL"

for data in sheet_data.prices['prices']:
    city = FlightSearch().get_destination_code(data['city'])
    data['iataCode'] = city

for data in sheet_data.prices['prices']:
    id = data['id']
    new_data = {
        "price": {
            "iataCode": data["iataCode"]
        }
    }
    sheet_data.update_sheet(new_data, id)

tomorrow = dt.datetime.now() + dt.timedelta(days = 1)
departure_range = tomorrow + dt.timedelta(days = 182.5)

for code in sheet_data.prices['prices']:
    flight_search_data = FlightSearch().search_flights(DEPARTURE_CITY_CODE, code["iataCode"], tomorrow, departure_range)
    print("hi", flight_search_data)
    if flight_search_data is not None and flight_search_data.price < code['lowestPrice']:
        NotificationManager().send_message()