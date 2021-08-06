import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import array as arr


	
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestCorrectAnswer():
	
	@pytest.mark.parametrize('listOfLinks', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
	def test_guest_should_enter_correct_answer(self, browser, listOfLinks):
		link = f"{listOfLinks}"
		browser.get(link)
		browser.implicitly_wait(10)
		input = browser.find_element_by_tag_name("textarea")
		input.send_keys(str(math.log(int(time.time()))))
		button = WebDriverWait(browser, 10).until(
		       EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
		)
		button.click()
		text_el = WebDriverWait(browser, 10).until(
			EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
		)
		message = text_el.text
		assert message == "Correct!", f"Answer is not correct, your message is {message} instead of 'Correct!'"
		print(message)

if __name__ == "__main__":

	pytest.main()







