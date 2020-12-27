from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo

# Use PyMongo to establish Mongo connection
conn = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(conn)

# Declare the database
db = client["Mars_db"]