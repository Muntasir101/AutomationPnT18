"""
step 1: Launch Browser
step 2: Go to Login page
step 3: Enter Email Address
step 4: Enter Password
step 5: Click Login button
step 6: Verification
step 7: Close browser
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# step 1: Launch Browser
driver = webdriver.Firefox()

# step 2: Go to Login page
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

# step 3: Enter Email Address
email = driver.find_element(By.ID, "input-email")
email.send_keys("mail123@gmail.com")
time.sleep(3)

# step 4: Enter Password
password = driver.find_element(By.ID, "input-password")
password.send_keys("12345655")

# step 5: Click Login button
login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
login_button.click()

# step 6: verify login
dashboard_url = "https://tutorialsninja.com/demo/index.php?route=account/account"
actual_url = driver.current_url

if actual_url == dashboard_url:
    print("Login Successful.")
else:
    print("Login Failed.")
    # Verify Login error message
    expected_login_error_Message = "Warning: No match for E-Mail Address and/or Password."

    error_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    actual_error_message_text = error_message.text

    if expected_login_error_Message == actual_error_message_text:
        print("Error Message Verified.")
    else:
        print("Test Fail.Error Message Verification Failed")

# step 7: Close browser
driver.quit()
