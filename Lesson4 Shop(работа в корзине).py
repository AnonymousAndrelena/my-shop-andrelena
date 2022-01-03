# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
# 4. Перейдите в корзину
# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
# 6. Нажмите на Undo (отмена удаления)
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
# 8. Нажмите на кнопку "UPDATE BASKET"
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии

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
# 2. Нажмите на вкладку "Shop"
Shop_tab = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/shop/"]').click()
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
#Проскроллили страницу вниз на 500 пикселей до видимости кнопке add to basket
driver.execute_script("window.scrollBy(0, 500);") # эта команда проскроллит страницу на 500 пикселей вниз
add_to_basket_HTML5_button = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=182"]').click()
time.sleep(2)
#Проскроллили страницу вниз на 500 пикселей до видимости кнопке add to basket
driver.execute_script("window.scrollBy(0, 500);") # эта команда проскроллит страницу на 500 пикселей вниз
add_to_basket_JS_button = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=180"]').click()
time.sleep(2)
# 4. Перейдите в корзину
go_basket_button = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/basket/"]').click()
# 5. Удалите первую книгу
# • Перед удалением добавьте sleep - я же Добавил явное ожидание be_clickable "крестика" закрытия
delete_basket_HTML5_button = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a")) ).click()
# 6. Нажмите на Undo (отмена удаления)
undo_delete_basket_HTML5_button = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div.woocommerce-message > a")) ).click()
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
Quantity_field = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input").clear()
Quantity_field_count = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
time.sleep(2)
Quantity_field_count.send_keys("3")
# 8. Нажмите на кнопку "UPDATE BASKET"
UPDATE_BASKET = driver.find_element_by_name("update_cart").click()
# 9. Добавьте тест, что атрибут value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
time.sleep(5)
quantity_check = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input") # нашли элемент по составному селектору
element_get_text = quantity_check.get_attribute("value") # получили аттрибут "value"
assert element_get_text == "3" # добавили проверку что содержимое равно ожидаемому
print("value равно =", element_get_text)
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
time.sleep(5)
APPLY_COUPON_button = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button").click()
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
coupon_code_text = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > ul > li")
coupon_code_text_check = coupon_code_text.text # получили текст элемента с помощью .text
assert coupon_code_text_check == "Please enter a coupon code." # добавили проверку что содержимое равно ожидаемому


