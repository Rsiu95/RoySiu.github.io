from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, os
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv("file_path")
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf4W4Hl4mL7WbNeH5swqAy2nPqsfgXCQCMNI5nZoT6PzUXH8A/viewform?usp=sf_link"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(executable_path=file_path, log_path="NUL"))

class AutoFill:
    def __init__(self):
        self.driver = driver.get(FORM_URL)
        
    def fill_application(self, housing_info_list):
        for info in housing_info_list:
            time.sleep(4)
            address_field = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
            print("Filling in:", info)
            time.sleep(1)
            address_field.send_keys(str(info[0]))
            time.sleep(1)
            price_field.send_keys(str(info[1]))
            time.sleep(1)
            link_field.send_keys(str(info[2]))
            time.sleep(2)
            submit_button.click()
            time.sleep(3)
            next_response = driver.find_element(by='xpath', value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            next_response.click()
            time.sleep(2)
        
        driver.quit()