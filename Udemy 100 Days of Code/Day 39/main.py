#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

sheet_data = DataManager()

#pprint(sheet_data.prices['prices'])

for data in sheet_data.prices['prices']:
    city = FlightSearch().get_destination_code(data['city'])
    data['iataCode'] = city

print(sheet_data.prices)
for data in sheet_data.prices['prices']:
    id = data['id']
    new_data = {
        "price": {
            "iataCode": data["iataCode"]
        }
    }
    sheet_data.update_sheet(new_data, id)