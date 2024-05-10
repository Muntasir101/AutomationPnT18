import pytest
import time
from selenium import webdriver
from Pytest.test_Login import *


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_logout(driver):
    test_launch_browser(driver)
    test_go_to_login_page(driver)
    test_enter_username(driver)
    test_enter_password(driver)
    test_click_login(driver)

    

