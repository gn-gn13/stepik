from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input[contains(@class, 'city')]").send_keys("Smolensk")
    browser.find_element(By.XPATH, "//input[@id='country']").send_keys("Russia")

    # Находим кнопку Submit и кликаем
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()