import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    #browser.switch_to.window(window_name)
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text

    print(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # У вас будет 30 секунд, чтобы увидеть число в алерте и вписать его на Stepik
    time.sleep(30)
    browser.quit()