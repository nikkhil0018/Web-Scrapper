import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

# I used Firefox; you can use whichever browser you like.
browser = webdriver.Firefox('/Users/nikkhil0018/Desktop/WebScrap')

# Tell Selenium to get the URL you're interested in.
browser.get("https://play.google.com/store?hl=en")

# Selenium script to scroll to the bottom, wait 3 seconds for the next batch of data to load, then continue scrolling.  It will continue to do this until the page stops loading new data.
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

# Now that the page is fully scrolled, grab the source code.
source_data = browser.page_source

# Throw your source into BeautifulSoup and start parsing!
bs_data = bs(source_data)