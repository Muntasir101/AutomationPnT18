import pytest
import time
from selenium import webdriver
from Pytest.test_login_valid import *


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_login2(driver):
    test_login_process(driver)
