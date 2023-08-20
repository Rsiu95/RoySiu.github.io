from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=options, service=Service(executable_path="C:/Users/RSiu9/OneDrive/Desktop/Chrome Development/chromedriver.exe", log_path="NUL"))
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# search = driver.find_element(by="class name", value = "cdx-text-input__input")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# stats = driver.find_element(by="xpath", value = '//*[@id="articlecount"]/a[1]')
# stats.click()

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(by="name", value = "fName")
last_name = driver.find_element(by="name", value = "lName")
email_address = driver.find_element(by="name", value = "email")
signup_button = driver.find_element(by="class name", value = "btn")
first_name.send_keys("John")
last_name.send_keys("Smith")
email_address.send_keys("john@smith.com")
signup_button.click()