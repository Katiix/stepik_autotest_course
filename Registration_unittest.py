from selenium import webdriver
import time
from time import sleep
import unittest

class TestAbs(unittest.TestCase):
	def test_reg1(self):
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)
			input1 = browser.find_element_by_css_selector("input:required.first")
			input1.send_keys("Ivan")
			input2 = browser.find_element_by_css_selector("input:required.second")
			input2.send_keys("ivanpetrov@mail.com")
			input2 = browser.find_element_by_css_selector("input:required.third")
			input2.send_keys("ivanpetrov@mail.com")
			button = browser.find_element_by_css_selector("button.btn")
			button.click()
			time.sleep(1)
			welcome_text_elt = browser.find_element_by_tag_name("h1")
			welcome_text = welcome_text_elt.text
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You should get congratulations message")
			time.sleep(10)
			browser.quit()
	def test_reg2(self):
			link = "http://suninjuly.github.io/registration2.html"
			browser = webdriver.Chrome()
			browser.get(link)
			input1 = browser.find_element_by_css_selector("input:required.first")
			input1.send_keys("Ivan")
			input2 = browser.find_element_by_css_selector("input:required.second")
			input2.send_keys("ivanpetrov@mail.com")
			input2 = browser.find_element_by_css_selector("input:required.third")
			input2.send_keys("ivanpetrov@mail.com")
			button = browser.find_element_by_css_selector("button.btn")
			button.click()
			time.sleep(1)
			welcome_text_elt = browser.find_element_by_tag_name("h1")
			welcome_text = welcome_text_elt.text
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You should get congratulations message")
			time.sleep(10)
			browser.quit()
if __name__ == "__main__":
    unittest.main()

