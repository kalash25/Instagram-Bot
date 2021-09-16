
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import urllib
import time
DRIVER_PATH = 'C:\path\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.minimize_window()

# followers, following and posts
def ffp(user):
    # getting the URL from user
    url = 'https://www.instagram.com/' + user
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")

    # to get the posts, follower count and following count
    data = soup.find_all('span', class_='g47SY')
    print("The number of posts are: ", data[0].text)
    print("The number of followers are: ", data[1].text)
    print("The number of following is: ", data[2].text)


def download_image(url, destination_given):
    destination = 'C:/Users/Kalash Jain/Desktop/insta/'
    destination_final = destination + destination_given
    resource = urllib.request.urlopen(url)
    file_name = destination_final + url[-8:] + '.jpg'
    output = open(file_name, 'wb')
    output.write(resource.read())
    output.close()


# profile pic downloader
def profile_pic(user):
    # getting the URL from user
    url = 'https://www.instagram.com/' + user
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")

    # to get the profile pic
    if soup.find('img', src=True, class_='_6q-tv') == None:  # incase of pvt accounts
        profile_pic_url = soup.find('img', src=True, class_='be6sR')['src']
    else:
        profile_pic_url = soup.find('img', src=True, class_='_6q-tv')['src']  # incase of public accounts

    # call to download profile pic
    download_image(profile_pic_url, 'profile_pics/')


def real_time(user):
    # getting the URL from user(to be written)
    url = 'https://www.instagram.com/' + user
    driver.get(url)

    # will have to manually end
    while (True):
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "lxml")

        # to get the following of famous accounts which keep changing
        data = soup.find_all('span', class_='g47SY')
        print(data[1]['title'])
        time.sleep(2)


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
    time.sleep(5)
    # to get rid of the save password pop up
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
        .click()
    time.sleep(5)

    try:
        # to get rid of the notifications pop up
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
    except:
        pass


def search_handles(search_name):
    search = driver.find_element_by_xpath('//input[@placeholder = "Search"]')
    search.send_keys(search_name)

    time.sleep(2)

    #handles = driver.find_elements_by_class_name('Ap253')
    handles = driver.find_elements_by_xpath('//span[@class = "Ap253"]')
    for i in handles:
        f = i.text
        if '#' not in f and ',' not in f:
            print(f)
    search.clear()


def open_profile(name):
    search = driver.find_element_by_xpath('//input[@placeholder = "Search"]')
    search.send_keys(name)
    time.sleep(3)
    profile = driver.find_element_by_xpath('//div[contains(@class, "fuqBx")]/a').get_attribute('href')
    driver.get(profile)

#def open_profile2(username) :
#    driver.get('https://www.instagram.com/'+ username+'/')


def follow(username):
    driver.get('https://www.instagram.com/' + username + '/')
    try:
        driver.find_element_by_xpath('//div[contains(@class, "_862NM")]/div/button')
        print('Already follow this account')

    except NoSuchElementException:
        driver.find_element_by_xpath("//button[contains(text(), 'Follow')]") \
            .click()
        print("started following {}".format(username))
        return


def unfollow(username):
    driver.get('https://www.instagram.com/' + username + '/')
    try:
        driver.find_element_by_xpath('//div[contains(@class, "_862NM")]/div/button')

        driver.find_element_by_xpath('//span[contains(@class, "vBF20 _1OSdk")]/button').click()  # To click on unfollow
        driver.find_element_by_xpath(
            '//div[contains(@class, "mt3GC")]/button').click()  # To check the unfollow dialogue box

    except NoSuchElementException:
        print('Already unfollowed this account')
        return

def like(username):
    driver.get('https://www.instagram.com/' + username + '/')
    driver.find_element_by_xpath('//div[contains(@class, "eLAPa")]').click()  ##To open the first post
    time.sleep(1)
    for i in range(2):
        bleh = driver.find_elements_by_class_name('_8-yf5 ')[8].get_attribute('aria-label')
        if bleh == 'Like':
            driver.find_element_by_xpath('//span[contains(@class, "fr66n")]/button').click()
        else:
            print('Already liked it')

        driver.find_elements_by_xpath('//div[contains(@class, "DdSX2")]/a')[-1].click()  ##To click on next post
        time.sleep(2)


def unlike(username):
    driver.get('https://www.instagram.com/' + username + '/')
    driver.find_element_by_xpath('//div[contains(@class, "eLAPa")]').click()  ##To open the first post
    time.sleep(1)
    for i in range(2):
        bleh = driver.find_elements_by_class_name('_8-yf5 ')[8].get_attribute('aria-label')
        if bleh == 'Unlike':
            driver.find_element_by_xpath('//span[contains(@class, "fr66n")]/button').click()

        else:
            print('Already unliked it')

        driver.find_elements_by_xpath('//div[contains(@class, "DdSX2")]/a')[-1].click()  ##To click on next post
        time.sleep(2)


# main
print("choose one of the options")
print("1. to get the follower,following and post count")
print("2. to download the profile pic ")
print("3. to get the real time follow count of an account")
print("4. to download the whole feed of some public account")
print("5. to login into instagram")
print("6. to search handles")
print("7. to open a profile")
print("8. to follow an account")
print("9. to unfollow an account")
print("10. to like a post")
print("11. to unlike a post")

x = int(input("enter your option: "))

if x == 1:
    user = input("Enter instagram handle: ")
    ffp(user)
elif x == 2:
    user = input("Enter instagram handle: ")
    profile_pic(user)
elif x == 3:
    user = input("Enter instagram handle: ")
    real_time(user)
elif x == 4:
    print("yet to be completed")
elif x == 5:
    login()
elif x == 6:
    search = input("enter the data to be searched for: ")
    login()
    search_handles(search)
elif x == 7:
    search = input("enter the profile name to be searched for: ")
    login()
    open_profile(search)
elif x == 8:
    search = input("Enter the profile you want to follow: ")
    login()
    follow(search)
elif x == 9:
    search = input("Enter the profile you want to unfollow: ")
    login()
    unfollow(search)
elif x == 10:
    search = input("Enter the profile: ")
    login()
    like(search)
elif x == 11:
    search = input("Enter the profile")
    login()
    unlike(search)
else:
    print("invalid input")








































'''



from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

# print(article.prettify())

# headline = article.h2.a.text
# print(headline)

# summary = article.find('div', class_='entry-content').p.text
# print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)


vid_id = vid_src.split('/')[4]
print(vid_id)

vid_id = vid_id.split('?')[0]
print(vid_id)


yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

'''