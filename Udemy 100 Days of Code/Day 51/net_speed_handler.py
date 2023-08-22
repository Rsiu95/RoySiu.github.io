from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv("file_path")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=file_path, log_path="NUL"))

class NetSpeed:
    def __init__(self):
        self.driver = driver.get("https://www.speedtest.net/")
        
    def press_start(self):
        start = driver.find_element(by = "class name", value = "start-text")
        start.click()
        
    def get_speed(self):
        speed = []
        download = driver.find_element(by="xpath", value = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload = driver.find_element(by='xpath', value = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        speed.append(download)
        speed.append(upload)
        return speed
