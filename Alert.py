from selenium import webdriver
import time
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    text_field=browser.find_element_by_css_selector("input[id='answer']")
    text_field.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()




