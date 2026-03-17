import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def fill_form(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test@mail.ru")

        # Отправляем форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)

        # Находим приветственный текст
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()
        return welcome_text

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.fill_form(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed on page 1")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.fill_form(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed on page 2")

if __name__ == "__main__":
    unittest.main()
