import smtplib
import datetime as dt
import random


current_time = dt.datetime.now()
current_year = current_time.year
current_month = current_time.month
current_day = current_time.weekday()

if current_day == 4:

    with open("./Udemy 100 Days of Code/Day 32/quotes.txt") as quotes:
        quote = quotes.readlines()
    
    def get_quote():
        quote_to_send = random.choice(quote)
        return quote_to_send

    quote_to_send = get_quote()
    test_gmail = "emailfortesting100days.01@gmail.com"
    gmail_password = "yxwyjtexeifjdecc"
    test_yahoo = "roy.siu@yahoo.com"

    # connect to the gmail server
    print("Connecting to the SMTP server...")
    try:
        connection_gmail = smtplib.SMTP("smtp.gmail.com", port = 587)
        print("Connection Successful!")
    except:
        print("Connection Failed.")

    print("Starting TLS")
    # Use to secure connection
    connection_gmail.starttls()
    print("TLS Started!")

    print("Logging in...")
    # login)
    connection_gmail.login(user = test_gmail, password = gmail_password)
    print("Login Successful!")

    # send mail
    connection_gmail.sendmail(from_addr = test_gmail, to_addrs = test_yahoo, msg = f"Subject: Friday Motivation\n\n{quote_to_send}")

    print("Closing connection...")
    # close connection
    connection_gmail.close()
    print("Connection closed!")
    
