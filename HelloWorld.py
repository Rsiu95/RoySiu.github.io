import keyboard
import pyautogui
import time


def auto_click():
    count = 0
    while True:
        pyautogui.click()
        count += 1
        time.sleep(0.5)
        print(count)
        if keyboard.is_pressed('esc'):
            break
                    

auto_click()
 