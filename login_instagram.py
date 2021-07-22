from selenium import webdriver
import time

DRIVER_PATH = 'C:\path\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.instagram.com/")

# logging in to instagram
time.sleep(2)
username = input("Enter username: ")
pw = input("enter password: ")
driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys(username)
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys(pw)

driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
time.sleep(2)
#to get rid of the save password pop up
driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
    .click()
time.sleep(2)

try:
    #to get rid of the notifications pop up
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()
except:
    pass

