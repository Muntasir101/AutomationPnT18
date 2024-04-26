from selenium import webdriver

# Launch Browser
driver = webdriver.Chrome()

# full window
driver.maximize_window()

# get window size
windowSize = driver.get_window_size()
print("Window Maximize Size: ", windowSize)

# get window position
windowPosition = driver.get_window_position(windowHandle='current')
print("Window Position: ", windowPosition)

# set window size
driver.set_window_rect(x=None, y=None, width=800, height=700)

# go to URL
driver.get("https://google.com")

# get current webpage title
pageTitle = driver.title
print("Page Title: ", pageTitle)

# get current page URL
pageUrl = driver.current_url
print("Current Page URL: ", pageUrl)

# close browser
driver.quit()
