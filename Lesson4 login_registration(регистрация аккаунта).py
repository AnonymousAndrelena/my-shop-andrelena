# Registration_login: регистрация аккаунта
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Register", введите email для регистрации
# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
# 5. Нажмите на кнопку "Register"

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
# 3. В разделе "Register", введите email для регистрации
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("Andrey@ya.ru")
# 4. В разделе "Register", введите пароль для регистрации
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("cfif99qwertyuiop[]")
#reg_password = WebDriverWait(driver, 30).until(
    #EC.text_to_be_present_in_element((By.ID, "reg_password"), "cfif99qwertyuiop"))
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
# 5. Нажмите на кнопку "Register"
time.sleep(5)
#reg_field = driver.find_element_by_class_name("woocomerce-FormRow")
#reg_field.click()
register_login = WebDriverWait(driver, 40).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocomerce-FormRow>input.woocommerce-Button")) )
#register_login = driver.find_element_by_css_selector(".woocomerce-FormRow>input.woocommerce-Button")
register_login.click()



