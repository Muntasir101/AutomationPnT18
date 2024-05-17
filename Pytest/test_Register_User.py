import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from python_random_strings import random_strings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = 'Ironman'


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


# 1. Launch browser
def test_launch_browser(driver):
    assert driver is not None


# 2. Navigate to url
def test_navigate_url(driver):
    driver.get('http://automationexercise.com')
    time.sleep(2)


# 3. Verify that home page is visible successfully
def test_verify_homepage(driver):
    expected_homepage_url = "https://automationexercise.com/"
    homepage_url = driver.current_url
    actual_homepage_url = homepage_url

    if actual_homepage_url == expected_homepage_url:
        print("Homepage is Visible Successfully")
    else:
        print("Homepage Visible Failed")


# 4. Click on Signup button
def test_click_signup_login_button(driver):
    signup_login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Signup / Login")))

    signup_login_button.click()


# 5. Verify 'New User Signup!' is visible
def test_verify_signup(driver):
    expected_signup = "New User Signup!"
    signup = driver.find_element(By.CSS_SELECTOR, ".signup-form > h2")
    actual_signup_text = signup.text

    if expected_signup == actual_signup_text:
        print("New User Signup is Visible Successfully")
    else:
        print("New User Signup Visible Failed")


# 6. Enter name and email address
def test_enter_username(driver):
    name = driver.find_element(By.NAME, "name")
    name.send_keys(username)
    time.sleep(2)


def test_enter_email_address(driver):
    email_address = driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")
    email_address.send_keys(random_strings.random_lowercase(10) + "@gmail.com")
    time.sleep(2)


# 7. Click 'Signup' button
def test_click_signup_button(driver):
    signup_button = driver.find_element(By.CSS_SELECTOR, "[action='\/signup'] .btn-default")
    signup_button.click()
    time.sleep(2)


# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
def test_verify_account_information(driver):
    expected_account_information = "ENTER ACCOUNT INFORMATION"
    account_information = driver.find_element(By.CSS_SELECTOR, ".login-form > .text-center.title > b")
    actual_account_information_text = account_information.text

    if expected_account_information == actual_account_information_text:
        print("ENTER ACCOUNT INFORMATION is Visible Successfully")
    else:
        print("ENTER ACCOUNT INFORMATION Visible Failed")


# 9. Fill details: Title, Name, Email, Password, Date of birth
def test_click_title_button(driver):
    title_button_mr = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > .top > .radio  input[name='title']")
    title_button_mr.click()
    time.sleep(2)


def test_enter_password(driver):
    password = driver.find_element(By.CSS_SELECTOR, "input#password")
    password.send_keys("654321")
    time.sleep(2)


def test_select_day(driver):
    day = driver.find_element(By.CSS_SELECTOR, "select#days")
    day_option = Select(day)

    # List all day
    all_day = [option.text for option in day_option.options]

    # Select Random day from list
    random_day = random.choice(all_day)
    day_option.select_by_visible_text(random_day)
    time.sleep(2)


def test_select_month(driver):
    month = driver.find_element(By.CSS_SELECTOR, "select#months")
    month_option = Select(month)

    # List all month
    all_month = [option.text for option in month_option.options]

    # Select Random day from list
    random_month = random.choice(all_month)
    month_option.select_by_visible_text(random_month)
    time.sleep(2)


def test_select_year(driver):
    year = driver.find_element(By.CSS_SELECTOR, "select#years")
    year_option = Select(year)

    # List all year
    all_year = [option.text for option in year_option.options]

    # Select Random day from list
    random_year = random.choice(all_year)
    year_option.select_by_visible_text(random_year)
    time.sleep(2)


# 10. Select checkbox 'Sign up for our newsletter!'
def test_click_news_letter_button(driver):
    newsletter_button = driver.find_element(By.CSS_SELECTOR, "input#newsletter")
    newsletter_button.click()
    time.sleep(2)


# 11. Select checkbox 'Receive special offers from our partners!'
def test_click_special_offers_button(driver):
    special_offers_button = driver.find_element(By.CSS_SELECTOR, "input#optin")
    special_offers_button.click()
    time.sleep(2)


# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
def test_enter_first_name(driver):
    first_name = driver.find_element(By.NAME, "first_name")
    first_name.send_keys(username)
    time.sleep(2)


def test_enter_last_name(driver):
    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys("Superhero")
    time.sleep(2)


def test_enter_company(driver):
    company = driver.find_element(By.NAME, "company")
    company.send_keys("Cocacola")
    time.sleep(2)


def test_enter_address(driver):
    address = driver.find_element(By.CSS_SELECTOR, "input[name = 'address1']")
    address.send_keys("Jamaica")
    time.sleep(2)


def test_enter_address2(driver):
    address2 = driver.find_element(By.CSS_SELECTOR, "input[name='address2']")
    address2.send_keys("New York")
    time.sleep(2)


def test_select_country(driver):
    country = driver.find_element(By.CSS_SELECTOR, "select#country")
    country_option = Select(country)

    # List all countries
    all_countries = [option.text for option in country_option.options]

    # Select Random country from list
    random_country = random.choice(all_countries)
    country_option.select_by_visible_text(random_country)
    time.sleep(2)


def test_enter_state(driver):
    state = driver.find_element(By.NAME, "state")
    state.send_keys("New York")
    time.sleep(2)


def test_enter_city(driver):
    city = driver.find_element(By.NAME, "city")
    city.send_keys("Jamaica")
    time.sleep(2)


def test_enter_zipcode(driver):
    zipcode = driver.find_element(By.CSS_SELECTOR, "input#zipcode")
    zipcode.send_keys("1200")
    time.sleep(2)


def test_enter_mobile(driver):
    mobile = driver.find_element(By.CSS_SELECTOR, "input#mobile_number")
    mobile.send_keys("121325457468")
    time.sleep(2)


# 13. Click 'Create Account button'
def test_click_Create_Account_button(driver):
    Create_Account_button = driver.find_element(By.CSS_SELECTOR,
                                                "section#form > .container form[method='post'] > .btn.btn-default")
    Create_Account_button.click()
    time.sleep(2)


# 14. Verify that 'ACCOUNT CREATED!' is visible
def test_verify_ACCOUNT_INFORMATION(driver):
    expected_ACCOUNT_INFORMATION = "ACCOUNT CREATED!"
    ACCOUNT_INFORMATION = driver.find_element(By.CSS_SELECTOR, ".text-center.title > b")
    actual_ACCOUNT_INFORMATION_text = ACCOUNT_INFORMATION.text

    if expected_ACCOUNT_INFORMATION == actual_ACCOUNT_INFORMATION_text:
        print("ACCOUNT CREATED is Visible Successfully")
    else:
        print("ACCOUNT CREATED Visible Failed")


# 15. Click 'Continue' button
def test_click_continue_button(driver):
    continue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    continue_button.click()
    time.sleep(5)


# 16. Verify that 'Logged in as username' is visible
def test_verify_username_visible(driver):
    expected_username_visible = "Logged in as " + username
    username_visible = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(10) > a")
    actual_username_visible_text = username_visible.text

    if expected_username_visible == actual_username_visible_text:
        print("Logged in as username is Visible Successfully")
    else:
        print("Logged in as username Visible Failed")
