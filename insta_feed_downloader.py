from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
import time

def download_image(url, destination_given):
    destination = 'C:/Users/Kalash Jain/Desktop/insta/'
    destination_final = destination + destination_given
    resource = urllib.request.urlopen(url)
    file_name = destination_final + url[-8:] + '.jpg'
    output = open(file_name, 'wb')
    output.write(resource.read())
    output.close()

#def indi_pic(lst):


#getting the URL from user(to be written)
username = input("Enter the instagram handle: ")
url = 'https://www.instagram.com/' + username

DRIVER_PATH = 'C:\path\chromedriver.exe'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.get(url)
soup =BeautifulSoup(driver.page_source, "lxml")

#to scroll to the end of a page
lenOfPage = driver.execute_script("window.scrollTo(0,document.body.scrollHeight); let lop = document.body.scrollHeight; return lop;")
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = driver.execute_script("window.scrollTo(0,document.body.scrollHeight); let lop = document.body.scrollHeight; return lop;")
    if lastCount == lenOfPage:
        match = True


#gets a list of links of all the posts
posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)


for link in posts:
    print(link)
    driver.get(link)
    srcc =  driver.find_element_by_xpath("//img[@class=\"FFVAD\"]").get_attribute("src")
    print(srcc)









