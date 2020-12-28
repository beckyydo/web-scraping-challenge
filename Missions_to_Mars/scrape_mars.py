#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser


# In[2]:

def scrape():
    executable_path = {'executable_path': 'chromedriver',}
    browser = Browser('chrome', **executable_path, headless=False)


# ## Step 1 - Scraping
# ### NASA Mars News

# In[3]:


# NASA Mars News
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)


# In[4]:


    browser.windows.current 


# In[5]:


# Get html of browser
    html = browser.html


# In[6]:


# Parse html
    soup = bs(html, 'html.parser')


# In[7]:


    # Get "div" tag class "content_page"
    content = soup.find("div", class_="content_page")

# In[8]:


# Get latest news title and paragraph
    title = content.find_all("div", class_= "content_title")
    news_title = title[0].text.strip()

# Display latest new title
    news_title


# In[9]:


# Get latest paragraph
    news_p = content.find("div", class_= 'article_teaser_body').text.strip()
# Display latest paragraph
    news_p


# In[10]:


    browser.quit()


# ### JPL Mars Space Images - Featured Image

# In[11]:


    executable_path = {'executable_path': 'chromedriver',}
    browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


# JPL Mars Space Images - Featured Image
    base_url = "https://www.jpl.nasa.gov"
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[13]:


# Visit url
    browser.visit(url)


# In[14]:


# Click FULL IMAGE
    browser.click_link_by_id('full_image')


# In[15]:


# Go to current window
    browser.windows.current 


# In[16]:


# Get html from browser
    html = browser.html


# In[17]:


# Parse html
    soup = bs(html, 'html.parser')


# In[18]:


# Find img tag
    img = soup.find("img", class_ = "fancybox-image")


# In[19]:


    img


# In[20]:


    featured_image_url = base_url + img['src']

# Display featured image url
    featured_image_url


# ### Mars Facts

# In[21]:


# Mars Facts
    url = "https://space-facts.com/mars/"
    browser.visit(url)


# In[22]:


    html = browser.html

# Parse html
    soup = bs(html, 'html.parser')


# In[23]:


# Extract html column as list
    col_1 = soup.find_all("td", class_ = "column-1")
    col_1 = [header.text for header in col_1]
    col_2 = soup.find_all("td", class_ = "column-2")
    col_2 = [header.text for header in col_2]


# In[24]:


# Create dataframe from extracted column
    mars_df = pd.DataFrame({"":col_1, " ":col_2})


# In[25]:


# Convert dataframe to html table
    table_html = mars_df.to_html(header=False)


# ### Mars Hemispheres

# In[26]:


# Vist url
    base_url = "https://astrogeology.usgs.gov"
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

# Get html of current browser
    html = browser.html

# Parse html
    soup = bs(html, "html.parser")


# In[27]:


# Find html with tag "a" and class "product-item"
    results = soup.find_all("a", class_ = "product-item")


# In[28]:


# Get the links for all the hemisphere
    image_links = []
    title = []
    for item in results:
        name = item.find("h3")
        if name != None:
            title.append(name.text)
            url_parameter = item['href']
            image_links.append(base_url+url_parameter)


# In[29]:


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
    
        # Display img_url
        hemisphere_image_urls


        # In[30]:


        browser.quit()

    scrape_dict = {
    "news_title": news_title,
    "news_p": news_p,
    "featured_image_url": featured_image_url,
    "table_html": table_html,
    "hemisphere_image_urls": hemisphere_image_urls
    }
    return scrape_dict




