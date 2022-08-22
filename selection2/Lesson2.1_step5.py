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

    # Считываем значение X (атрибут текст считывает текст между тегами)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)


    # Вводим число в поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Ставим галочку
    button = browser.find_element(By.ID, 'robotCheckbox')
    button.click()

    # Выбираем Robots rule!
    button = browser.find_element(By.ID, 'robotsRule')
    button.click()

    # Нажимаем Submit
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()