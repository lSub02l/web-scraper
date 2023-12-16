from selenium import webdriver
import gspread

AUTH_KEY = "C://Users//mrzeq//Downloads//googleauth.json"

# Selenium driver init
driver = webdriver.Chrome()
url = "https://www.apartments.com/new-york-ny/800-to-2500/"
driver.get(url)

# Downloading elements
listings = driver.find_elements_by_class_name("name")

# Google sheets init
gc = gspread.service_account(filename=AUTH_KEY)
sh = gc.open('renting_data')
worksheet = sh.sheet1

# Saving data 
row = 1
for listing in listings:
    address = listing.find_element_by_class_name("propertyAddress")
    price = listing.find_element_by_class_name("rentPrice")

    worksheet.update(f'A{row}', address)
    worksheet.update(f'B{row}', price)
    row += 1

driver.quit()