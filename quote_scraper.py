from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)   # leiab Chromedriveri PATH-ist
driver.get("https://quotes.toscrape.com")
time.sleep(1)
for quote in driver.find_elements("class name", "text"):
    print(quote.text)
driver.quit()