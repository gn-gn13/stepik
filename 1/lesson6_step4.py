from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/find_link_text"
x = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:

    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.PARTIAL_LINK_TEXT, x)
    link.click()
    # 1. По тегу (Tag Name)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    # 2. По атрибуту name
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    # 3. По имени класса (Class Name)
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    # 4. По ID (уже было в шаблоне)
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Кнопка
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # У вас будет 30 секунд, чтобы увидеть число в алерте и вписать его на Stepik
    time.sleep(30)
    browser.quit()
