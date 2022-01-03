# Shop: количество товаров в категории
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте категорию "HTML"
# 5. Добавьте тест, что отображается три товара

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
# 4. Откройте категорию "HTML"
HTML_category = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product-category/html/"]').click()
# 5. Добавьте тест, что отображается три товара
all_options = driver.find_elements_by_tag_name("img")
for option in all_options:
    print("отображаются книги на этой странице:", option.get_attribute("title"))


