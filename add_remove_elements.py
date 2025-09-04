from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)   # leiab Chromedriveri PATH-ist
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(1)
button = driver.find_element("xpath", "//button[text()='Add Element']")
for i in range(5):
    button.click()
    time.sleep(.5)
time.sleep(1)
for button in driver.find_elements("class name", "added-manually"):
    button.click()
    time.sleep(.5)
driver.quit()