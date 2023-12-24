from selenium import webdriver
from selenium.webdriver.common.by import By
import gspread

#AUTH_KEY = "C://Users//mrzeq//Downloads//googleauth.json"
AUTH_KEY = "C://Users//bazyl//Desktop//googleauth.json"

# Selenium driver init
driver = webdriver.Chrome()
url = "https://www.apartments.com/new-york-ny/800-to-2500/"
driver.get(url)

# Google sheets init
gc = gspread.service_account(filename=AUTH_KEY)
sh = gc.open('renting_data')
worksheet = sh.sheet1

listings = driver.find_elements("placard")

# Saving data 
for listing in listings:
    address_element = listing.find_element_by_css_selector(".property-address.js-url")
    address = address_element.text.strip()

    price_element = listing.find_element_by_class_name("property-rents")
    price = price_element.text.strip()

    beds_element = listing.find_element_by_class_name("property-beds")
    beds = beds_element.text.strip()

    print(f"Address: {address}\nPrice: {price}\nBeds: {beds}\n")

driver.quit()