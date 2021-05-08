#All import packages that need to be imported
import requests
from bs4 import BeautifulSoup
import time
import threading
import pymongo
from pymongo import MongoClient
import redis

#Connection to our mongoDB client, specify which database we want to use and which collection we want to add data to
cluster = MongoClient("mongodb://127.0.01:27017")
db = cluster["DBA"]
collection = db["HashValues"]

client = redis.Redis(host = '127.0.0.1', port = 6379)

#Function that we will loop over every minute
def scraper():
    records = client.get("HashValues")
    print(records)
    #Sort the records list by the value of the Bitcoin which sits at position 2 of the list
    records.sort(key=lambda x:x[2])

    Create a JSON object (post) from our highest value Hash and insert it into our collection "HashValues"
    post = {"Hash": records[-1][0], "Time": records[-1][1], "BTC": records[-1][2], "USD": records[-1][3]}
    print(post)
    collection.insert_one(post)

    #Confirmation our data is added to our collection
    print("Added to collection")

    #Timer that makes sure this code is run every minute
    time.sleep(60)
    
#Loop        
while True:
    scraper()