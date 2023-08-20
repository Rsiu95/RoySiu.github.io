from selenium import webdriver
from selenium.webdriver.chrome.service import Service
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=options, service=Service(executable_path="C:/Users/RSiu9/OneDrive/Desktop/Chrome Development/chromedriver.exe", log_path="NUL"))

# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# dollar_price = driver.find_element(by="class name", value = "a-price-whole")
# cents_price = driver.find_element(by="class name", value = "a-price-fraction")
#print(f"${dollar_price.text}.{cents_price.text}")
#test = driver.find_elements(By.XPATH,'//*[@id="corePrice_feature_div"]/div')

driver.get("https://www.python.org/")
shrubbery = driver.find_elements(by="class name", value = "shrubbery")
upcoming_events = shrubbery[1].text.split("\n")
upcoming_events.remove("Upcoming Events")
upcoming_events.remove("More")

new_list = []
for index in range(len(upcoming_events)):
    if index == 0 or index % 2 == 0:
        time = upcoming_events[index]
        name = upcoming_events[index + 1]
    
        new_list.append({
            "time": time,
            "name": name
            })
        
upcoming_events_dict = {}
for index, items in enumerate(new_list):
    upcoming_events_dict.update({
        index : items
    })
print(upcoming_events_dict)
driver.quit()
