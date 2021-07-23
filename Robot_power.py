from selenium import webdriver
import time
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    text_field=browser.find_element_by_css_selector("input[id='answer']")
    text_field.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()





