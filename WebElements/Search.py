
from selenium import webdriver
from selenium.webdriver.common.by import By

# step 1: Launch Browser
driver = webdriver.Firefox()

# step 2: Go to Login page
driver.get("https://tutorialsninja.com/demo/index.php?route=product/search&search=macbook")

driver.find_element(By.CSS_SELECTOR, "#content [class='product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12']:nth-of-type(3) .hidden-md").click()
expected_success_message = "Success: You have added MacBook Pro to your shopping cart!"
actual_success_message = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible").text
print(actual_success_message)

if expected_success_message == actual_success_message:
    print("Product Add success")
else:
    print("Product add failed")


#cart_text = " 1 item(s) - $2,000.00"
cart_text = driver.find_element(By.CSS_SELECTOR, "div#cart > .btn.btn-block.btn-inverse.btn-lg.dropdown-toggle").text
print(cart_text)

quantity = cart_text.split(" - ")[0]
print(quantity)  # 1 item(s)

price = cart_text.split(" - ")[1]
print(price)  # $2,000.00

# remove $ from price and convert to float
product_price_withoutDollar = price.replace("$", "")
product_price_withoutDollar_withoutComma = product_price_withoutDollar.replace(",","")
print(product_price_withoutDollar) # 2,000.00
print(product_price_withoutDollar_withoutComma) # 2000.00
actual_price = float(product_price_withoutDollar_withoutComma)
print(actual_price) # 2000.0


product_quantity = int(quantity.split()[0])
print(product_quantity)  # 1

actual_cost = product_quantity * product_price_withoutDollar_withoutComma
print("Price Shown in Cart: ", actual_cost)


