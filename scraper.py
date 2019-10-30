from bs4 import BeautifulSoup
import requests

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
# print(soup.prettify())
# match = soup.title.text
# match = soup.find('div')
# match = soup.find('div', class_='footer')
# article = soup.find('div', class_='article')
# print(article)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print(' ')