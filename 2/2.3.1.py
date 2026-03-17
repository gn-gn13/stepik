import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
try:

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # У вас будет 30 секунд, чтобы увидеть число в алерте и вписать его на Stepik
    time.sleep(30)
    browser.quit()
