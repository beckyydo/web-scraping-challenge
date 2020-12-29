import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time

def scrape():
    executable_path = {'executable_path': 'chromedriver',}
    browser = Browser('chrome', **executable_path, headless=False)
    # NASA Mars News
    url = "https://mars.nasa.gov/news"
    browser.visit(url)
    time.sleep(5)
    # Get html of browser
    html = browser.html
    # Parse html
    soup = bs(html, 'html.parser')
    # Get "div" tag class "content_page"
    content = soup.find("div", class_="content_page")
    # Get latest news title and paragraph
    title = content.find_all("div", class_= "content_title")
    news_title = title[0].text.strip()
    # Get latest paragraph
    news_p = content.find("div", class_= 'article_teaser_body').text.strip()

    base_url = "https://www.jpl.nasa.gov"
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # Visit url
    browser.visit(url)
    # Click FULL IMAGE
    browser.click_link_by_id('full_image')
    time.sleep(5)
    # Get html from browser
    html = browser.html
    # Parse html
    soup = bs(html, 'html.parser')
    # Find img tag
    img = soup.find("img", class_ = "fancybox-image")
    # Featured image url
    featured_image_url = base_url + img['src']

    # Mars Facts
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    time.sleep(5)
    mars = pd.read_html(url)
    table_html = mars[0].to_html(header=False)
    
    # Vist url
    base_url = "https://astrogeology.usgs.gov"
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    # Get html of current browser
    html = browser.html
    time.sleep(5)
    # Parse html
    soup = bs(html, "html.parser")
    # Find html with tag "a" and class "product-item"
    results = soup.find_all("a", class_ = "product-item")
    # Get the links for all the hemisphere
    image_links = []
    title = []
    for item in results:
        name = item.find("h3")
        if name != None:
            title.append(name.text)
            url_parameter = item['href']
            image_links.append(base_url+url_parameter)
    # Function to get the dictionary of image url and title
    hemisphere_image_urls = []

    for i in range(len(title)):
        # Remove Enhanced From Title
        image_title = title[i][:len(title)-13]
        # Click image
        browser.visit(image_links[i])
        # Click Sample
        browser.click_link_by_text('Sample')
        # Go to next page (Sample page) to get url
        window = browser.windows[0]
        image_url = window.next.url
        window.close()
        # Create dictionary and append to list
        img_dict = {'title': image_title,
        'img_url': image_url}
        hemisphere_image_urls.append(img_dict)
    
    browser.quit()

    scrape_dict = {
    "news_title": news_title,
    "news_p": news_p,
    "featured_image_url": featured_image_url,
    "table_html": table_html,
    "hemisphere_image_urls": hemisphere_image_urls
    }
    return scrape_dict




