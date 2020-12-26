import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Step 1 - Scraping
# NASA Mars News
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)
html = browser.html

# Parse html
soup = bs(html, 'html.parser')

# Get latest news title and paragraph
content_title = soup.find_all("div", class_="content_title")

for title in content_title:
    try:
        news_title = title.find("a").text.strip()
        break
    except:
        pass

# Display latest new title
print(news_title)

# Get latest paragraph
news_p = soup.find("div", class_= 'article_teaser_body').text.strip()

# Display latest paragraph
print(news_p)