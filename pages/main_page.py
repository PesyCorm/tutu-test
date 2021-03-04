from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def input_area(driver):
	return WebDriverWait(driver, 10).until(
		EC.presence_of_element_located(
			(By.TAG_NAME, "input")
			)
		)

def get_result_button(driver):
	return WebDriverWait(driver, 10).until(
		EC.presence_of_element_located(
			(By.TAG_NAME, "button")
			)
		)

def result_text(driver):
	return WebDriverWait(driver, 10).until(
		EC.presence_of_element_located(
			(By.ID, "old")
			)
		).text