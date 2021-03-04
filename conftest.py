from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def driver(request):

    driver = webdriver.Chrome()
    driver.get("http://tutu-ru.github.io/")
    request.addfinalizer(driver.quit)
    return driver