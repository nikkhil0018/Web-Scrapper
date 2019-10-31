import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

# I used Firefox; you can use whichever browser you like.
browser = webdriver.Firefox('/usr/local/bin')

# Tell Selenium to get the URL you're interested in.
browser.get("https://play.google.com/store/search?q=medicine%20app&c=apps")

csv_file = open('appData.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['NAME', 'URL', 'EMAIL'])

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
    print(appEmail)
    # appRating = newSoup.find(class_='pf5lIe')
    # appRating = appRating.find()['aria-label']
    # appDisc = newSoup.find(class_='IQ1z0d').text
    # print(appRating)
    # print(appDisc)

    csv_writer.writerow([appName,appUrl,appEmail])

    print('------------------------------------------')

csv_file.close()
print('****DONE*****DONE*******DONE******')

# <div class="b8cIId ReQCgd Q9MA7b"><a href="/store/apps/details?id=com.e_steps.herbs"><div class="WsMG1c nnK0zc" title="Herbs Encyclopedia">Herbs Encyclopedia</div></a><div class="cqtbn"></div></div>


# < div class = "b8cIId ReQCgd Q9MA7b" > < a href = "/store/apps/details?id=com.medicinal.herbs.plant" > < div class = "WsMG1c nnK0zc" title = "Medicinal Plants &amp; Herbs" > Medicinal Plants & amp; Herbs < / div > < / a > < div class = "cqtbn" > < / div > < / div >
