from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "https://SunInJuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    # 3. По имени класса (Class Name)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button.click()

finally:
    # У вас будет 30 секунд, чтобы увидеть число в алерте и вписать его на Stepik
    time.sleep(30)
    browser.quit()
