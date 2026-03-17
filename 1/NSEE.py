from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Сначала проверяем на первой ссылке, затем меняем на registration2.html для проверки бага
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля, используя уникальные связки классов
    # Поле First Name
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")

    # Поле Last Name
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Petrov")

    # Поле Email
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("test@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент с приветственным текстом
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Проверяем, что текст совпадает с ожидаемым
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ждем 10 секунд для визуального контроля и закрываем браузер
    time.sleep(10)
    browser.quit()