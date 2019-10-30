from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://play.google.com/store/search?q=fitness%60apps&c=apps&hl=en').text

csv_file = open('appData.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['NAME', 'URL', 'EMAIL', 'RATING'])

soup = BeautifulSoup(source, 'lxml')

# <div class="b8cIId ReQCgd Q9MA7b"><a href="/store/apps/details?id=com.e_steps.herbs"><div class="WsMG1c nnK0zc" title="Herbs Encyclopedia">Herbs Encyclopedia</div></a><div class="cqtbn"></div></div>

# item = soup.find(class_='Q9MA7b')
# appName = item.find('div', class_='nnK0zc').text
# appUrl = item.find('a')['href']
# appUrl = 'https://play.google.com{}'.format(appUrl)
# print(appName)
# print(appUrl)

# newSource = requests.get(appUrl).text
# newSoup = BeautifulSoup(newSource, 'lxml')
# appEmail = newSoup.find('a', class_='euBY6b').text
# appRating = newSoup.find(class_='pf5lIe')
# appRating = appRating.find()['aria-label']
# appDisc = newSoup.find(class_='IQ1z0d').text
# print(appEmail)
# print(appRating)
# print(appDisc)

for item in soup.find_all(class_='Q9MA7b'):
    appName = item.find('div', class_='nnK0zc').text
    appUrl = item.find('a')['href']
    appUrl = 'https://play.google.com{}'.format(appUrl)
    print(appName)
    print(appUrl)

    newSource = requests.get(appUrl).text
    newSoup = BeautifulSoup(newSource, 'lxml')
    appEmail = newSoup.find('a', class_='euBY6b').text
    appRating = newSoup.find(class_='pf5lIe')
    appRating = appRating.find()['aria-label']
    # appDisc = newSoup.find(class_='IQ1z0d').text
    print(appEmail)
    print(appRating)
    # print(appDisc)

    csv_writer.writerow([appName, appUrl, appEmail, appRating])

    print('------------------------------------------')

csv_file.close()
print('****DONE*****DONE*******DONE******')

# <div class="b8cIId ReQCgd Q9MA7b"><a href="/store/apps/details?id=com.e_steps.herbs"><div class="WsMG1c nnK0zc" title="Herbs Encyclopedia">Herbs Encyclopedia</div></a><div class="cqtbn"></div></div>


# < div class = "b8cIId ReQCgd Q9MA7b" > < a href = "/store/apps/details?id=com.medicinal.herbs.plant" > < div class = "WsMG1c nnK0zc" title = "Medicinal Plants &amp; Herbs" > Medicinal Plants & amp; Herbs < / div > < / a > < div class = "cqtbn" > < / div > < / div >
