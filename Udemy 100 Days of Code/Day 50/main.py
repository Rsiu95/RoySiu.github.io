from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, os
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv("file_path")
USER = os.getenv("USER")
P_WORD = os.getenv("P_WORD")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=options, service=Service(executable_path=file_path, log_path="NUL"))

driver.get("https://tinder.com/")
base_window = driver.window_handles[0]

time.sleep(2)
login_button = driver.find_element(by="xpath", value='//*[@id="q1298270057"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()
time.sleep(2)
fb_login = driver.find_element(by = "xpath", value = '//*[@id="q-430111019"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
fb_login.click()
time.sleep(5)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
login_email = driver.find_element(by="id", value = "email")
password = driver.find_element(by="id", value = "pass")
login_email.send_keys(str(USER))
password.send_keys(str(P_WORD))
time.sleep(3)
fb_login_button = driver.find_element(by="id", value = "loginbutton")
fb_login_button.click()

time.sleep(5)
driver.switch_to.window(base_window)
location_share = driver.find_element(by = "xpath", value = '//*[@id="q-430111019"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
location_share.click()
time.sleep(5)
notifications_button = driver.find_element(by = "xpath", value='//*[@id="q-430111019"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
notifications_button.click()
time.sleep(2)

while True:
    time.sleep(3)
    try:
        nope_button = driver.find_element(by="xpath", value = '//*[@id="q1298270057"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button/span/span')
    except:
        nope_button = driver.find_element(by="xpath", value = '//*[@id="q1298270057"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')
    nope_button.click()
        



