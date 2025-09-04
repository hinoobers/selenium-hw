from selenium import webdriver
import time

query = input("Mida soovid otsida?")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)   # leiab Chromedriveri PATH-ist
driver.get("https://www.google.com")
time.sleep(1)

# Accept all
try:
    button = driver.find_element("id", "L2AGLb")
    button.click()
    time.sleep(1)
except:
    print("Nuppu ei leitud")


element = driver.find_element("id", "APjFqb") # textarea
print(element.tag_name)
element.send_keys(query)
element.send_keys("\n")  # press enter./
print(driver.title)
input("Vajuta ENTER, et sulgeda brauser")