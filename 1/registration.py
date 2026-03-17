from selenium import webdriver
#ввести pip install selenium в терминал и не потребуется устанавливать driver в ручную
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//form/div[3]/input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, "//form/div[4]/input")
    input4.send_keys("Russia")
    button_send = browser.find_element(By.XPATH, "//form/div[6]/button[3]")
    button_send.click()

finally:
    time.sleep(5)
    browser.quit()
