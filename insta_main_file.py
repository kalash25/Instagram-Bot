
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



username = input("Enter the instagram handle: ")
url = 'https://www.instagram.com/' + username

DRIVER_PATH = 'C:\path\chromedriver.exe'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.get(url)
soup =BeautifulSoup(driver.page_source, "lxml")





'''
#to get the profile pic
if soup.find('img', src=True, class_='_6q-tv') == None:  #incase of pvt accounts
    profile_pic_url = soup.find('img', src=True, class_='be6sR')['src']
else:
    profile_pic_url = soup.find('img', src=True, class_='_6q-tv')['src'] #incase of public accounts

#call to download profile pic
download_image(profile_pic_url,'profile_pics/')
'''



#to get the posts, follower count and following count
data = soup.find_all('span', class_='g47SY')
print("The number of posts are: ", data[0].text)
print("The number of followers are: ", data[1].text)
print("The number of following is: ", data[2].text)




        


'''
links = []
for i in soup.find_all('a', href = True):
    if i['href'].startswith('/p'):
        print("link found: https://www.instagram.com{0}".format(i['href']))
        links.append('https://www.instagram.com' + i['href'])

print(links)

'''


'''
driver2 = webdriver.Chrome(executable_path = DRIVER_PATH)
driver2.get(links[1])
#print(driver2.page_source)
soup2 = BeautifulSoup(driver2.page_source, "lxml")
bleh = soup2.find_all('div', class_='eLAPa _23QFA')[0].find_all('img')[0]['src']
#print(soup2)

'''



#download_image('https://instagram.fdel42-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/119938164_179604643723713_7668721752459704883_n.jpg?_nc_ht=instagram.fdel42-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=aR8-VT2E540AX-Fo21r&_nc_tp=19&oh=e012eadfc85b4dcd91138ab3ac38bc83&oe=5F935767')
driver.quit()
#driver2.quit()
