import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from python_random_strings import random_strings

# step 1: Launch Browser
driver = webdriver.Firefox()

# step 2: Go to Login page
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
time.sleep(2)

firstName = driver.find_element(By.CSS_SELECTOR, "input#input-firstname")
firstName.send_keys(random_strings.random_lowercase(5))

lastName = driver.find_element(By.CSS_SELECTOR, "input#input-lastname")
lastName.send_keys("Selenium")

email = driver.find_element(By.CSS_SELECTOR, "#input-email")
email.send_keys(random_strings.random_lowercase(10) + "@gmail.com")

telephone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
telephone.send_keys("123456")

password = driver.find_element(By.CSS_SELECTOR, "#input-password")
password.send_keys("1234567")

confirmPassword = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
confirmPassword.send_keys("1234567")

privacy = driver.find_element(By.CSS_SELECTOR, "input[name='agree']")
privacy.click()

continueButton = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
continueButton.click()

# Verify account create success message
expected_Success_Message = "Your Account Has Been Created!"

success_message = driver.find_element(By.CSS_SELECTOR, "#content h1")
actual_success_message_text = success_message.text

if expected_Success_Message == actual_success_message_text:
    print("Test Pass.Account Created Successfully")
else:
    print("Test Fail.Account Creation Failed")
