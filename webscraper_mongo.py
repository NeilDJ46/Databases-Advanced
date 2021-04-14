#All import packages that need to be imported
import requests
from bs4 import BeautifulSoup
import time
import threading
import pymongo
from pymongo MongoClient

#Connection to our mongoDB client, specify which database we want to use and which collection we want to add data to
cluster = MongoClient("mongodb://127.0.01:27017")
db = cluster["DBA"]
collection = db["HashValues"]

#Function that we will loop over every minute
def scraper():
    #Define the page we want to scrape
    url = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
    page = BeautifulSoup(url.content, 'html.parser')

    #Make a list that will hold all records that are in the div that holds all items we want to scrape
    items = page.findAll("div", {"class":"sc-6nt7oh-0 PtIAf"})
    records = [] #Empty list in which we will store our different records on the page as lists (will create Lists in List)

    length = (len(items)//4) - 1

    #Loop over the items in the items list
    for i in range(length):
        #Temporary list that will be filled with the 4 items we want to scrape of the record at position i and append this new list in the records list
        temp = []
        temp.append(items[i*4].text)
        temp.append(items[(i*4) + 1].text)
        temp.append(items[(i*4) + 2].text)
        temp.append(items[(i*4) + 3].text)
        records.append(temp)

    #Sort the records list by the value of the Bitcoin which sits at position 2 of the list
    records.sort(key=lambda x:x[2])

    #Create a JSON object (post) from our highest value Hash and insert it into our collection "HashValues"
    post = {"Hash": records[-1][0], "Time": records[-1][1], "BTC": records[-1][2], "USD": records[-1][3]}
    collection.insert_one(post)

    #Confirmation our data is added to our collection
    print("Added to collection")

    #Timer that makes sure this code is run every minute
    time.sleep(60)
    
#Loop        
while True:
    scraper()