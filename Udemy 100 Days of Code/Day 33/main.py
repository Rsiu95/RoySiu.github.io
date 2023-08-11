import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_location = (iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#print(data)
time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

print(time_now.hour)
# user details
my_email = "EMAIL HERE"
my_password = "PASSWORD HERE"

if (time_now.hour == sunrise or time_now.hour == sunset) and (iss_latitude <= (parameters["lat"] + 5) or \
    (iss_latitude >= (parameters["lat"] - 5)) and (iss_longitude <= (parameters["lng"] + 5) or \
    (iss_longitude >= (parameters["lng"] - 5)))):
    print("Connecting to the SMTP server...")
    try:
        connection = smtplib.SMTP("smtp.gmail.com", port = 587)
        print("Connection Successful!")
    except:
        print("Connection Failed.")

    # Use to secure connection
    print("Starting TLS")
    connection.starttls()
    print("TLS Started!")

    # login
    print("Logging in...")
    connection.login(user = my_email, password = my_password)
    print("Login Successful!")

    # send mail to each recipient
    connection.sendmail(
        from_addr = my_email,
        to_addrs = "roy.siu@yahoo.com",
        msg = f"Subject: Look up!\n\n The ISS is above you."
        )
    print("Email successfully sent!")

