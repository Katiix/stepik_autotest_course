from selenium import webdriver
import time
import math
from time import sleep
link = " http://suninjuly.github.io/find_link_text.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)                                                #open a link in a browser
	link = browser.find_element_by_link_text("224592")               #find a link with text "224592"
	link.click()
	input1 = browser.find_element_by_tag_name("input")               #find input field with tag name "input"
	input1.send_keys("Ivan")                                         #fill in the input field
	input2 = browser.find_element_by_name("last_name")
	input2.send_keys("Petrov")
	input3 = browser.find_element_by_class_name("city")
	input3.send_keys("Smolensk")
	input4 = browser.find_element_by_id("country")
	input4.send_keys("Russia")
	button = browser.find_element_by_css_selector("button.btn")      #find button with class btn
	button.click()						         #click the button
finally:
	time.sleep(30)
	browser.quit()



