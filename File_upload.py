from selenium import webdriver
import time
import os
from time import sleep
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[name="email"]')
    input3.send_keys("ivanpetrov@mail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4 = browser.find_element_by_css_selector('input[type="file"]')
    input4.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()


