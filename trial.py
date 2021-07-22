'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import urllib
import time

DRIVER_PATH = 'C:\path\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)



def login():
    user = input("Enter instagram handle: ")
    pw = input("Enter password: ")

    driver.get("https://www.instagram.com/")

    # logging in to instagram
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name=\"username\"]") \
        .send_keys(user)
    driver.find_element_by_xpath("//input[@name=\"password\"]") \
        .send_keys(pw)

    driver.find_element_by_xpath('//button[@type="submit"]') \
        .click()
    time.sleep(4)
    # to get rid of the save password pop up
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
        .click()
    time.sleep(2)

    try:
        # to get rid of the notifications pop up
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
    except:
        pass


def followers_list(username):
    driver.get('https://www.instagram.com/' + username + '/')
    time.sleep(1)
    driver.execute_script('document.documentElement.scrollTop=0;')  # To scroll to the top of the page

    # to click on the follower button
    driver.find_element_by_xpath('//a[contains(@class, "-nal3 ")]/span').click()

    time.sleep(2)

    followers_panel = driver.find_element_by_class_name('isgrP')
    len_followers = len(followers_panel.find_elements_by_css_selector('li'))
    h1 = len_followers
    # To scroll down the dialog box
    while True:
        h2 = h1
        new_height = driver.execute_script("return arguments[0].scrollHeight", followers_panel)
        driver.execute_script("arguments[0].scrollTo(0, arguments[1]);", followers_panel, new_height)
        len_followers = len(followers_panel.find_elements_by_css_selector('li'))
        h1 = len_followers
        if h1 == h2:
            break;

    follow_list = driver.find_elements_by_class_name('uu6c_')

    follower = set()
    for i in range(len(follow_list)):
        user = follow_list[i].find_element_by_class_name('_0imsa').text
        follower.add(user)

    print(len(follower))

login()
followers_list('overspilled_')
'''



