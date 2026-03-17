from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    title = browser.find_element(By.ID, "input_value").text
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(title))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    button.click()


finally:
    # Ждем 10 секунд для визуального контроля и закрываем браузер
    time.sleep(10)
    browser.quit()