import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

executable_path = {'executable_path': 'chromedriver',}
browser = Browser('chrome', **executable_path, headless=False)