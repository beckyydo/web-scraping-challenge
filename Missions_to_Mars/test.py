# Define scrape function
def scrape():
    # Execute scrape_test.py 
    from scrape_test import news_title, news_p, featured_image_url, table_html, hemisphere_image_urls

    # Return one Python dictionary of all scraped data
    scrape_dict = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "table_html": table_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    return scrape_dict

print(scrape())
