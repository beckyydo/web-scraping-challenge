# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
## import scrape_mars
# Execute scraping code
import scrape

# Define scrape function
def scrape():
    # Return one Python dictionary of all scraped data
    scrape_dict = {"News Title": news_title,
                    "News Paragraph": news_p,
                    "Featured Image Url": featured_image_url,
                    "Table HTML": table_html,
                    "Hemisphere Name & URL": hemisphere_image_urls
    }
    return scrape

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
    # Return template and data
    return render_template("index.html")


# Route that will run scrape function
@app.route("/scrape")
def scrape_info():
    # Run scrape function
    scrape_data = scrape()

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
