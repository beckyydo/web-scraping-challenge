# Import dependencies
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

# Create instance of Flask
app = Flask(__name__)

# Connect to Mars database in Mongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

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
    scrape_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scrape_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
