# Home: добавление комментария
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку "SUBMIT"

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# импортируем webdriver
from selenium import webdriver
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe") # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
# Настройте открытие окон в полный размер,
driver.maximize_window() #открытие окон в полный размер, с помощью этой команды
driver.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2. Проскролльте страницу вниз на 600-700 пикселей
time.sleep(2)
driver.execute_script("window.scrollBy(0, 700);") # эта команда проскроллит страницу на 600 пикселей вниз
time.sleep(2)
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
Selenium_Ruby = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product/selenium-ruby/"]')
Selenium_Ruby.click() # команда нужна для нажатия(клика) на элемент
# 4. Нажмите на вкладку "REVIEWS"
driver.execute_script("window.scrollBy(0, 500);") # эта команда проскроллит страницу на 500 пикселей вниз
time.sleep(2)
REVIEWS_button = driver.find_element_by_xpath('//a[@href="#tab-reviews"]')
REVIEWS_button.click() # команда нужна для нажатия(клика) на элемент
# 5. Поставьте 5 звёзд
star_5 = driver.find_element_by_class_name("star-5")
star_5.click()
# 6. Заполните поле "Review" сообщением: "Nice book!"
Review_field = driver.find_element_by_id("comment")
# заполним поле "Review"
Review_field.send_keys("Nice book!")
# 7. Заполните поле "Name"
driver.execute_script("window.scrollBy(0, 300);") # эта команда проскроллит страницу на 300 пикселей вниз
time.sleep(2)
Mame_field = driver.find_element_by_id("author")
Mame_field.send_keys("Andrey")
# 8. Заполните "Email"
email_field = driver.find_element_by_id("email")
email_field.send_keys("Andrey@ya.ru")
# 9. Нажмите на кнопку "SUBMIT"
driver.execute_script("window.scrollBy(0, 200);") # эта команда проскроллит страницу на 200 пикселей вниз
SUBMIT_button = driver.find_element_by_id("submit")
SUBMIT_button.click()

