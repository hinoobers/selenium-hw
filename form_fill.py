from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)   # leiab Chromedriveri PATH-ist
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(1)
username = driver.find_element("id", "username") # username kast
password = driver.find_element("id", "password") # parooli kast

# Sisestame andmed
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
time.sleep(1)

loginbtn = driver.find_element("class name", "radius") # login nupp
loginbtn.click()
time.sleep(1)
if(driver.page_source.find("You logged into a secure area!") != -1): # kontrollime kas tuli tekst you logged into secure area
    print("Sisselogimine õnnestus")
else:
    print("Sisselogimine ebaõnnestus")
driver.quit()