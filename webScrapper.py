from bs4 import BeautifulSoup
import requests
import csv

# source = requests.get('http://coreyms.com').text

# soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

# article = soup.find('article')
# print(article.prettify())    

# headline = article.h2.a.text
# print(headline)

# summary = article.find('div', class_='entry-content').p.text
# print(summary)

# vid_src = article.find('iframe', class_='youtube-player')['src']
# print(vid_src)

# vid_id = vid_src.split('/')
# print(vid_id)

# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')
# print(vid_id)

# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# print(vid_id)

# yt_link = f'https://youtube.com/watch?v={vid_id}' python 3.6 or higher

# yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)
# print(yt_link)


source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cmsScrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video_link'])



for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)
    except Exception as e:
        # pass
        yt_link = None
    print(yt_link)
    print(' ')

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()