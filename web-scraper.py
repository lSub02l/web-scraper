from selenium import webdriver

# Selenium driver init
driver = webdriver.Chrome()
url = "https://www.apartments.com/new-york-ny/800-to-2500/"
driver.get(url)

driver.quit()