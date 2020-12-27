def scrape():
    import scrape
    scrape_dict = {"News Title": news_title,
                    "News Paragraph": news_p,
                    "Featured Image Url": featured_image_url,
                    "Table HTML": table_html,
                    "Hemisphere Name & URL": hemisphere_image_urls
    }
    return scrape