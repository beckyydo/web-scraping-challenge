# Import dependencies
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo

# Define scrape function
def scrape():
    # Execute scrape_test.py 
    from scrape_test import news_title, news_p, featured_image_url, table_html, hemisphere_image_urls
    #import scrape_mars

    # Return one Python dictionary of all scraped data
    scrape_dict = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "table_html": table_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    return scrape_dict

# Create instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.Mars_db

# Connect to Mars database in Mongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_db")

# Route to render index.html using data from Mongo
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", news = mars_data)


# Route that will run scrape function
@app.route("/scrape")
def scrape_info():
    # Run scrape function
    scrape_data = scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scrape_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
