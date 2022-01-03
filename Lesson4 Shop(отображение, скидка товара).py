# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "Android Quick Start Guide"
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)

import time
# импортируем класс Select или библиотеки webdriver
from selenium.webdriver.support.select import Select
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
# 4. Откройте книгу "Android Quick Start Guide"
#Проскролльте страницу вниз на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);") # эта команда проскроллит страницу на 300 пикселей вниз
time.sleep(2)
Android_Quick_Start_Guide = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product/android-quick-start-guide/"]').click()
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
element_old_price = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span") # нашли элемент по составному селектору
element_get_text = element_old_price.text # получили текст элемента с помощью .text
assert element_get_text == "₹600.00" # добавили проверку что содержимое равно ожидаемому
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
element_new_price = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span") # нашли элемент по составному селектору
element_get_text = element_new_price.text # получили текст элемента с помощью .text
assert element_get_text == "₹450.00" # добавили проверку что содержимое равно ожидаемому
# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
Android_Quick_Start_Guide_tutle_btn = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169 > div.images > a > img")) ).click()
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
krestik_btn = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a")) ).click()
driver.quit() # команда quit() – нужна для закрытия всех вкладок и завершения процесса webdriver
