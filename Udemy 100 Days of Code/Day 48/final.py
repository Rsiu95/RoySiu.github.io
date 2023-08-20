from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv("file_path")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=options, service=Service(executable_path=file_path, log_path="NUL"))

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)
language_EN = driver.find_element(by="id", value = "langSelect-EN")
language_EN.click()
time.sleep(10)

bigcookie = driver.find_element(by="id", value = "bigCookie")
cookies = driver.find_element(by="id", value = "cookies")
prices = driver.find_elements(by="class name", value = "price")
shop = driver.find_elements(by="class name", value = "product")

def get_prices(shop):
    prices = []
    for price in shop:
        cost = price.find_element(by="class name", value = "price")
        value = cost.text
        if "million" in value:
            value = (value.split(" ")[0]) * 1000000
        if "," in value:
            value = value.replace(",","")
        try:
            prices.append([int(value), price])
        except:
            pass
    return prices

timeout = time.time() + 5
five_min = time.time() + 60*5
running = True
while running:
    bigcookie.click()
    if time.time() > timeout:
        prices = get_prices(shop)
        num_cookies = int(cookies.text.split()[0].replace(",",""))
        for value in prices[::-1]:
            if num_cookies - value[0] > 0:
                click_shop = value[1]
                click_shop.click()
                break
        timeout = time.time() + 5
        
    if time.time() > five_min:
        cookies_ps = driver.find_element(by="id", value = "cookiesPerSecond")
        print("finished with cookies " + cookies_ps.text)
        running = False
        break

driver.quit()

    
