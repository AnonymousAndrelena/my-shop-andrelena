# Registration_login: логин в систему
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# 5. Нажмите на кнопку "Login"
# 6. Добавьте проверку, что на странице есть элемент "Logout"

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
# 2. Нажмите на вкладку "My Account Menu"
My_Account_Menu_tab = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/my-account/"]')
My_Account_Menu_tab.click()
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
username_field = driver.find_element_by_id("username")
username_field.send_keys("Andrey@ya.ru")
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
password_field = driver.find_element_by_id("password")
password_field.send_keys("cfif99qwertyuiop")
# 5. Нажмите на кнопку "Login"
Login_button = driver.find_element_by_name("login")
Login_button.click()
# 6. Добавьте проверку, что на странице есть элемент "Logout"
# находим элементе Logout
Logout_element = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/my-account/customer-logout/"]')
# добавили проверку что слово "Logout" содержится в элементе Logout
Logout_element_text = Logout_element.text # получили текст элемента Logout с помощью .text
assert Logout_element_text == "Logout"

