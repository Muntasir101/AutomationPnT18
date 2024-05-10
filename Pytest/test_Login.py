import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_launch_browser(driver):
    assert driver is not None


def test_go_to_login_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)


def test_enter_username(driver):
    username = driver.find_element(By.NAME, "username")
    username.send_keys("Admin")


def test_enter_password(driver):
    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin123")


def test_click_login(driver):
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    login_button.click()
    time.sleep(3)


def test_verify_login(driver):
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url

    if actual_url == dashboard_url:
        print("Login Successful.")
    else:
        print("Login Failed.")

        # Verify Login error message
        expected_login_error_Message = "Invalid credentials"

        error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text")
        actual_error_message_text = error_message.text

        if expected_login_error_Message == actual_error_message_text:
            print("Error Message Verified.")
        else:
            print("Test Fail.Error Message Verification Failed")
