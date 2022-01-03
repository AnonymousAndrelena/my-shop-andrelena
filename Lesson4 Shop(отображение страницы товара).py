# Shop: отображение страницы товара
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "HTML 5 Forms"
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"

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
# 2. Залогиньтесь
My_Account_Menu_tab = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/my-account/"]')
My_Account_Menu_tab.click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("Andrey@ya.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("cfif99qwertyuiop")
#Нажмите на кнопку "Login"
Login_button = driver.find_element_by_name("login").click()
# 3. Нажмите на вкладку "Shop"
Shop_tab = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]').click()
# 4. Откройте книгу "HTML 5 Forms"
#Проскролльте страницу вниз на 600-700 пикселей
driver.execute_script("window.scrollBy(0, 700);") # эта команда проскроллит страницу на 600 пикселей вниз
HTML_5_Forms = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product/html5-forms/"]').click()
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
HTML5_Forms = driver.find_element_by_class_name("product_title")
# добавили проверку что слово "Logout" содержится в элементе Logout
HTML5_Forms_text = HTML5_Forms.text # получили текст элемента Logout с помощью .text
assert HTML5_Forms_text == "HTML5 Forms"
if HTML5_Forms_text == "HTML5 Forms":
 print("Заголовок книги называется:",HTML5_Forms_text)
else:
 print("Заголовок книги не",HTML5_Forms_text)

