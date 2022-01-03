# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# 4. Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
# 5. Перейдите в корзину
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

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
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
#Проскроллили страницу вниз на 500 пикселей до видимости кнопке add to basket
driver.execute_script("window.scrollBy(0, 500);") # эта команда проскроллит страницу на 500 пикселей вниз
time.sleep(2)
add_to_basket_button = driver.find_element_by_xpath('//a[@href="/shop/?add-to-cart=182"]').click()
# 4. Добавьте тест, что возле корзины(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
time.sleep(2)
amount_to_basket = driver.find_element_by_css_selector("#wpmenucartli > a > span.cartcontents") # нашли элемент по составному селектору
element_get_text = amount_to_basket.text # получили текст элемента с помощью .text
assert element_get_text == "1 Item" # добавили проверку что содержимое равно ожидаемому
price_to_basket = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount") # нашли элемент по составному селектору
element_get_text = price_to_basket.text # получили текст элемента с помощью .text
assert element_get_text == "₹180.00" # добавили проверку что содержимое равно ожидаемому
# 5. Перейдите в корзину
view_to_basket_button = driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/basket/"]').click()
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
element_Subtotal = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span"), "₹180.00"))
print("Subtotal отобразилась стоимость", element_Subtotal)
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
time.sleep(2)
element_Total = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span"), "₹189.00"))
print("Total отобразилась стоимость", element_Total)
driver.quit() # команда quit() – нужна для закрытия всех вкладок и завершения процесса webdriver

