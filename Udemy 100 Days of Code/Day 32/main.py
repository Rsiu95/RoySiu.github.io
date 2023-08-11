import smtplib
import datetime as dt
import random
import pandas

# user details
my_email = "emailfortesting100days.01@gmail.com"
my_password = 

# get birthday dates, name and email from birthdays.csv
birthday_data = pandas.read_csv("./Udemy 100 Days of Code/Day 32/birthdays.csv")
birthday_info = birthday_data.to_dict(orient = "records")

# get today's date
current_time = dt.datetime.now()
while current_time:
    
    current_day = current_time.day
    current_month = current_time.month

    # choose a random template from /letter_templates
    random_letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    with open("./Udemy 100 Days of Code/Day 32/letter_templates/" + random.choice(random_letter), "r") as template:
        letter = template.read()
        
    recipient_details = []
    for data in birthday_info:
        #print(data)
        if current_day == int(data["day"]) and current_month == int(data["month"]):
            details = {
                "name":data["name"],
                "email":data["email"]
            }
            recipient_details.append(details)

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
    for recipient in recipient_details:
        print(f"Sending message to {recipient['name']}")
        updated_message = letter.replace("[NAME]", recipient["name"])
        connection.sendmail(
            from_addr = my_email,
            to_addrs = recipient["email"],
            msg = f"Subject: Happy Birthday {recipient['name']}!\n\n {updated_message}"
        )
        print("Email successfully sent!")
    
    break
