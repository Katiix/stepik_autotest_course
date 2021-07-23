from selenium import webdriver
import time
from time import sleep
import math
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector("[id='num1']").text
    y = browser.find_element_by_css_selector("[id='num2']").text
    sum = str(int(x)+int(y))
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(sum)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()

