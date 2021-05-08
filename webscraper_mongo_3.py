#All import packages that need to be imported
import requests
from bs4 import BeautifulSoup
import time
import threading
import pymongo
from pymongo import MongoClient
import redis
import math

#Connection to our mongoDB client, specify which database we want to use and which collection we want to add data to
cluster = MongoClient("mongodb://127.0.01:27017")
db = cluster["DBA"]
collection = db["HashValues"]

client = redis.Redis(host = '127.0.0.1', port = 6379)

#Function that we will loop over every minute
def scraper():
    hashes = list(map(str, r.lrange("Hash", 0, -1)))
    times = list(map(str, r.lrange("Time", 0, -1)))
    btc = list(map(str, r.lrange("Bitcoin value", 0, -1)))
    dollar = list(map(float, r.lrange("Dollar value", 0, -1)))
    max_dollar = max(dollar)
    index = dollar.index(maxd)
    max_hash = hashes[index]
    max_time = times[index]
    max_btc = btc[index]
    
    highest_value = {"Hash": max_hash, "Time": max_time, "BTC": max_btc, "Dollar": max_dollar}
    print(highest_value)

    collection.insert_one(highest_value)

    time.sleep(60)
    
#Loop        
while True:
    scraper()