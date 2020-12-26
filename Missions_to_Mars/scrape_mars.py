#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser


# In[2]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# ## Step 1 - Scraping
# ### NASA Mars News

# In[3]:


# NASA Mars News
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)
html = browser.html

# Parse html
soup = bs(html, 'html.parser')


# In[4]:


# Get latest news title and paragraph
content_title = soup.find_all("div", class_="content_title")

for title in content_title:
    try:
        news_title = title.find("a").text.strip()
        break
    except:
        pass

# Display latest new title
news_title


# In[5]:


# Get latest paragraph
news_p = soup.find("div", class_= 'article_teaser_body').text.strip()

# Display latest paragraph
news_p


# ### JPL Mars Space Images - Featured Image

# In[6]:


# JPL Mars Space Images - Featured Image
base_url = "https://www.jpl.nasa.gov"
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[7]:


# Click FULL IMAGE
browser.click_link_by_id('full_image')


# In[8]:


html = browser.html

# Parse html
soup = bs(html, 'html.parser')


# In[9]:


img = soup.find_all("img", class_ = "fancybox-image")[0]
featured_image_url = base_url + img['src']

# Display featured image url
featured_image_url


# ### Mars Facts

# In[10]:


# Mars Facts
url = "https://space-facts.com/mars/"
browser.visit(url)


# In[11]:


html = browser.html

# Parse html
soup = bs(html, 'html.parser')


# In[12]:


# Extract html column as list
col_1 = soup.find_all("td", class_ = "column-1")
col_1 = [header.text for header in col_1]
col_2 = soup.find_all("td", class_ = "column-2")
col_2 = [header.text for header in col_2]


# In[13]:


# Create dataframe from extracted column
mars_df = pd.DataFrame({"":col_1, " ":col_2})


# In[14]:


# Convert dataframe to html table
table_html = mars_df.to_html(header=False)


# ### Mars Hemispheres

# In[15]:


# Vist url
base_url = "https://astrogeology.usgs.gov"
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)

# Get html of current browser
html = browser.html

# Parse html
soup = bs(html, "html.parser")


# In[16]:


# Find html with tag "a" and class "product-item"
results = soup.find_all("a", class_ = "product-item")


# In[17]:


# Get the links for all the hemisphere
image_links = []
title = []
for item in results:
    name = item.find("h3")
    if name != None:
        title.append(name.text)
        url_parameter = item['href']
        image_links.append(base_url+url_parameter)


# In[18]:


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


# In[ ]:




