# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
# 5. Отсортируйте товары от большего к меньшему
# • в селекторах используйте класс Select
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# 7. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
# • Используйте проверку по value

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
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
Default_sorting = driver.find_element_by_css_selector("[value='menu_order']") # "Default_sorting" это просто название переменной
# Найдём атрибут "selected" с помощью встроенного метода get_attribute и проверим его значение:
Default_sorting_checked = Default_sorting.get_attribute("selected")
print("Default sorting: ", Default_sorting_checked)
if Default_sorting_checked is not None:
 print("Selector сортировки по умолчанию отмечен")
else:
 print("Selector сортировки по умолчанию НЕ отмечен")
# 5. Отсортируйте товары от большего к меньшему
# • в селекторах используйте класс Select
price_desc = driver.find_element_by_class_name("orderby")
select = Select(price_desc)  #Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_visible_text("Sort by price: high to low") # ищет элемент по видимому тексту, ищем элемент с текстом "Sort by price: high to low"
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
Default_sorting_new = driver.find_element_by_css_selector("[value='price-desc']")
# 7. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему #content > form > select > option:nth-child(6)
# • Используйте проверку по value ([value='price-desc'])
# Найдём атрибут "selected" с помощью встроенного метода get_attribute и проверим его значение:
Default_sorting_new_checked = Default_sorting_new.get_attribute("orderby")
print("Текущий выбор селектора: ", Default_sorting_new_checked)
if Default_sorting_checked is not None:
 print("Selector сортировки Sort by price: high to low")
else:
 print("Selector сортировки не Sort by price: high to low")
