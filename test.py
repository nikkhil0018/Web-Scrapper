import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

# I used Firefox; you can use whichever browser you like.
browser = webdriver.Firefox('/usr/local/bin')

# Tell Selenium to get the URL you're interested in.
browser.get("https://play.google.com/store/search?q=herb&c=apps")

csv_file = open('HerbUSA.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['NAME', 'URL', 'EMAIL', 'RATING'])

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match==False):
                lastCount = lenOfPage
                time.sleep(3)
                lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True

# Now that the page is fully scrolled, grab the source code.
source = browser.page_source

source=source.encode('ascii', 'ignore')
soup = BeautifulSoup(source, 'lxml')

for item in soup.find_all(class_='Q9MA7b'):
    appName = item.find('div', class_='nnK0zc').text
    appUrl = item.find('a')['href']
    appUrl = 'https://play.google.com{}'.format(appUrl)
    print(appName)
    print(appUrl)

    newSource = requests.get(appUrl).text
    newSoup = BeautifulSoup(newSource, 'lxml')
    appEmail = newSoup.find('a', class_='euBY6b').text
    # appDisc = newSoup.find(class_='IQ1z0d').text
    print(appEmail)
    # print(appDisc)

    try:
        appRating = newSoup.find(class_='pf5lIe')
        appRating = appRating.find()['aria-label']
    except Exception as e:
        appRating = None

    print(appRating)
    print('------------------------------------------')
    csv_writer.writerow([appName,appUrl,appEmail, appRating])

csv_file.close()
print('-----DONE*****DONE*****DONE******DONE*****DONE-----')
