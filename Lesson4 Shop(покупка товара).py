# Shop: покупка товара
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Перейдите в корзину
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# 8. Нажмите PLACE ORDER
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# # 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"

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
# 3. Добавьте в корзину книги "HTML5 WebApp Development"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
#Проскроллили страницу вниз на 500 пикселей до видимости кнопке add to basket
driver.execute_script("window.scrollBy(0, 500);") # эта команда проскроллит страницу на 500 пикселей вниз
add_to_basket_HTML5_button = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=182"]').click()
time.sleep(2)
# 4. Перейдите в корзину
go_basket_button = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/basket/"]').click()
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
PROCEED_TO_CHECKOUT_button = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-forward")) ).click()
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
first_name_field = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")) ).send_keys("Andrey")
last_name_field = driver.find_element_by_name("billing_last_name").send_keys("Mat")
billing_company_field = driver.find_element_by_name("billing_company").send_keys("Matex")
billing_email_field = driver.find_element_by_name("billing_email").send_keys("a@ya.ru")
billing_phone_field = driver.find_element_by_name("billing_phone").send_keys("+79045555555")
#Проскроллили страницу вниз на 500 пикселей до видимости кнопке add to basket
driver.execute_script("window.scrollBy(0, 500);") # эта команда проскроллит страницу на 500 пикселей вниз
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# selector_country = driver.find_element_by_css_selector("#select2-chosen-1").click()
# search_field_country = driver.find_element_by_id("s2id_autogen1_search").send_keys("Samoa")
# chose_country = driver.find_element_by_id("s2id_autogen1_search").click()

#select = Select(driver.find_element_by_xpath('/html/body/span')).select_by_value('WS')
billing_address_1 = driver.find_element_by_id("billing_address_1").send_keys("Lenina")
billing_city = driver.find_element_by_id("billing_city").send_keys("Апиа")
billing_state = driver.find_element_by_id("billing_state").send_keys("Самоа")
billing_postcode = driver.find_element_by_id("billing_postcode").send_keys("190005")

# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
#Проскроллили страницу вниз на 500 пикселей до видимости кнопке add to basket
driver.execute_script("window.scrollBy(0, 600);") # эта команда проскроллит страницу на 600 пикселей вниз
time.sleep(5)
Check_Payments = driver.find_element_by_css_selector("[value='cheque']").click()
# 8. Нажмите PLACE ORDER
#Проскроллили страницу вниз на 300 пикселей до видимости кнопке add to basket
driver.execute_script("window.scrollBy(0, 300);") # эта команда проскроллит страницу на 300 пикселей вниз
time.sleep(5)
place_order_button = driver.find_element_by_id("place_order").click()
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
Thank_you_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
Check_Payments_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > ul > li.method > strong"), "Check Payments"))
driver.quit() # команда quit() – нужна для закрытия всех вкладок и завершения процесса webdriver
