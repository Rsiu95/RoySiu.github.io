from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, os
from twitter_handler import TwitterHandler
from net_speed_handler import NetSpeed
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv("file_path")
USER = os.getenv("USER")
P_WORD = os.getenv("P_WORD")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
promised_speed = [100, 20]
net_speed = NetSpeed()

time.sleep(2)
net_speed.press_start()
time.sleep(60)
speed = net_speed.get_speed()

twitter = TwitterHandler()
time.sleep(5)
twitter.login()
time.sleep(5)
if float(speed[0]) < promised_speed[0] or float(speed[1]) < promised_speed[1]:
    message = f"Hey @[provider], why is my internet speed {speed[0]}down\\{speed[1]}up when I pay for {promised_speed[0]}down\\{promised_speed[1]}?"
    twitter.send_tweet(message)