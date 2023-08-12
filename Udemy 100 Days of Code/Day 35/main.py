import requests
import datetime as dt
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = "YOURAPIKEY"
account_sid = "YOUR ACCOUNT SID"
auth_token = "AUTH_TOKEN"

weather_api = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=-37.814&lon=144.9633&appid={YOURAPIKEY}")

data = weather_api.json()

# weather_params = {
#     "lat": -37.814,
#     "long": 144.9633,
#     "appid": API_KEY,
# }

# OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# weather_api = requests.get(OWM_endpoint, params = weather_params)

# data = weather_api.json()
# print(data)

forecast = []
for weather_data in data["list"]:
    for status in weather_data["weather"]:
        forecast.append({
            "weather_id": status["id"],
            "time": weather_data["dt_txt"]
        })

# Get the current date and time
current_date = dt.datetime.now()
#print(current_date.day)
# Calculate the date after 2 days
two_days_later = current_date + dt.timedelta(days=2)

hours_delta = dt.timedelta(hours=48)
two_days_later_48_hours = current_date + hours_delta

for day in forecast:
    print(day["weather_id"])
    if day["weather_id"] <= 700:
        date = day["time"].split("-")[2].split(" ")[0]
        today = current_date.day
        if int(date) == today:
            print("It will rain today.")
            will_rain = True
            
if will_rain:
    # for trial twilio accounts
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    
    # above not needed if paid service
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "It's going to rain today. Bring an umbrella",
        from_ = "+12345678",
        to = "+1234567"
    )
    print(message.status)
        
    