from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
import time


#getting the URL from user(to be written)
username = input("Enter the instagram handle: ")
url = 'https://www.instagram.com/' + username

DRIVER_PATH = 'C:\path\chromedriver.exe'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

driver.get(url)
driver.maximize_window()
driver.minimize_window()


# will have to manually end
while(True):

    driver.get(url)
    soup =BeautifulSoup(driver.page_source, "lxml")

    # to get the following of famous accounts which keep changing
    data = soup.find_all('span', class_='g47SY')
    print(" current follower count: ",data[1]['title'])
    time.sleep(2)

