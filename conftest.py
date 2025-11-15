
import pytest
from selenium import webdriver


@pytest.fixture (params=["chrome","firefox","edge"])
def driver (request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

