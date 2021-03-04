from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Скрипт для получения элементов со страницы
# Предусловие: страница должна быть запущена, каждая функция принимает на вход объект вебдрайвера
# input_area() возвращает элемент поля ввода
# get_result_button() возвращает элемент кнопки "Посчитать"
# result_text() возвращает текст результата

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