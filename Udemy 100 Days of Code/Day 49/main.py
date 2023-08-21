from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time, os
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv("file_path")
username = os.getenv("username")
password = os.getenv("password")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=options, service=Service(executable_path=file_path, log_path="NUL"))

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3688143967&f_AL=true&f_C=%5B%5D&f_CM=%5B%5D&f_E=%5B%5D&f_EA=%5B%5D&f_F=%5B%5D&f_I=%5B%5D&f_JC=%5B%5D&f_JIYN=%5B%5D&f_JT=%5B%5D&f_PP=%5B%5D&f_T=%5B%5D&f_WT=%5B%5D&keywords=python%20developer&sortBy=R")

time.sleep(6)
sign_in_button = driver.find_element(by = "xpath", value = "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()
time.sleep(3)

username = driver.find_element(by="xpath", value = '//*[@id="username"]')
username.send_keys(username)
password = driver.find_element(by="xpath", value = '//*[@id="password"]')
password.send_keys(password)

second_sign_in = driver.find_element(by="xpath", value = '//*[@id="organic-div"]/form/div[3]/button') 
second_sign_in.click()
time.sleep(3)

easy_apply_buttons = driver.find_elements(by = "css selector", value = 'jobs-apply-button')
time.sleep(3)
for button in easy_apply_buttons:
    button.click()
    time.sleep(3)
    mobile = driver.find_element(by="xpath", value = '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3688143967-95331133-phoneNumber-nationalNumber"]')
    mobile.send_keys("0412345678")
    time.sleep(3)

    next_button = driver.find_element(By.CSS_SELECTOR, ".display-flex .artdeco-button")
    next_button.click()
    time.sleep(3)
    next_button.click()
    time.sleep(3)
    try:
        next_button.click()
    except:
        exit_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        exit_button.click()
        time.sleep(3)
        discard_button = driver.find_element(By.CSS_SELECTOR,".artdeco-modal__actionbar button")
        discard_button.click()
    time.sleep(3)