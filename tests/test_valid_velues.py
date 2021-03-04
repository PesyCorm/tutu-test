import pytest
from pages import *

# Скрипт для тестирования страницы http://tutu-ru.github.io/
# При старте открывается браузер (по умолчанию Chrome), переходит на тестируемую страницу
# В поле ввода даты рождения поочередно вводит даты из параметризации, сравнивая с ожидаемым результатом
# В случае несовпадения, выводит текст ошибки с датой рождения и ожидаемым результатом

@pytest.mark.parametrize("date, expected_result",
                         [("11.01.2000", "21"), ("13.07.1999", "21"), ("20.09.2007", "13")]
                         )
def test_check_results(driver, date, expected_result):
    inp_obj = input_area(driver)
    btn_obj = get_result_button(driver)

    inp_obj.send_keys(date)
    btn_obj.click()
    assert expected_result in result_text(
        driver), f"Ожидалось, что для даты рождения {date} возраст будет равен {expected_result}"

    inp_obj.clear()
