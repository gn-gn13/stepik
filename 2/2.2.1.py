from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    title = browser.find_element(By.ID, "num1").text
    title1 = browser.find_element(By.ID, "num2").text
    tit = str(int(title) + int(title1))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(tit)  # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    button.click()


finally:
    # Ждем 10 секунд для визуального контроля и закрываем браузер
    time.sleep(10)
    browser.quit()