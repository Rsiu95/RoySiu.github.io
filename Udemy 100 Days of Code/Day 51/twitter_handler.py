import time, os
import net_speed_handler
from dotenv import load_dotenv
load_dotenv()

file_path = os.getenv("file_path")
USER = os.getenv("USER")
P_WORD = os.getenv("P_WORD")
D_NAME = os.getenv("D_NAME")
driver = net_speed_handler.driver

class TwitterHandler:
    def __init__(self):
        self.driver = driver.get("https://twitter.com/")
        
    def login(self):
        sign_in = driver.find_element(by = 'xpath', value = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        sign_in.click()
        time.sleep(3)
        user = driver.find_element(by='xpath', value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user.send_keys(str(USER))
        time.sleep(2)
        next_button = driver.find_element(by = 'xpath', value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(2)
        try:
            user_pass = driver.find_element(by='xpath', value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            user_pass.send_keys(str(P_WORD))
        except:
            verify = driver.find_element(by='xpath', value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            verify.send_keys(str(D_NAME))
            time.sleep(2)
            verify_button = driver.find_element(by='xpath', value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            verify_button.click()
        time.sleep(2)
        user_pass = driver.find_element(by='xpath', value = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        user_pass.send_keys(str(P_WORD))
        
        login = driver.find_element(by='xpath', value ='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login.click()
    
    def send_tweet(self, message):
        tweet_box = driver.find_element(by='xpath', value = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(message)
        time.sleep(2)
        post = driver.find_element(by='xpath', value = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        time.sleep(2)
        post.click()