from selenium import webdriver
import time
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    res = calc(int(x))
    check = browser.find_element_by_css_selector("input[id='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton.click()
    text_field=browser.find_element_by_css_selector("input[id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(res)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  
    button.click()
    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()