from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)   # leiab Chromedriveri PATH-ist
driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

checkboxes = driver.find_element("link text", "Checkboxes") # Leiame linkide seast "Checkboxes" lingi
checkboxes.click()

time.sleep(.5)

checkboxes = driver.find_elements("css selector", "input[type='checkbox']") # Kõik checkboxid
for checkbox in checkboxes:
    if(not checkbox.is_selected()): # Üks on juba selected, ärme unselecti seda
        checkbox.click()
    time.sleep(.5)
time.sleep(1.5)
driver.back()
time.sleep(1)
driver.quit()