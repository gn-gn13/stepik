from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("calc(x)")

    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("calc(x)")

    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("calc(x)")

    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = r"C:\Users\user\Desktop\file.txt"
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # У вас будет 30 секунд, чтобы увидеть число в алерте и вписать его на Stepik
    time.sleep(30)
    browser.quit()
