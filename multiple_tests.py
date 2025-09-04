from selenium import webdriver
import undetected_chromedriver as uc
import time

query = input("Mida soovid otsida mõlemalt search enginest?")

def test_brave():
    driver = webdriver.Chrome()
    driver.get("https://search.brave.com")
    time.sleep(1)

    element = driver.find_element("id", "searchbox") # textarea
    print(element.tag_name)
    element.send_keys(query)
    element.send_keys("\n")  # press enter./
    time.sleep(1)
    driver.quit()

def test_duckduckgo():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com")
    time.sleep(1)
    element = driver.find_element("name", "q") # textarea
    print(element.tag_name)
    element.send_keys(query)
    element.send_keys("\n")  # press enter./
    time.sleep(1)
    driver.quit()

test_duckduckgo()
time.sleep(1)
test_brave()