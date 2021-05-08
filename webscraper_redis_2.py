#All import packages that need to be imported
import requests
from bs4 import BeautifulSoup
import time
import threading
import redis
import json

#Connection to Reddis to specify which port we will send our data to
client = redis.Redis(host = '127.0.0.1', port = 6379)

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

    #Convert this from a Python object to a JSON string and cache it into Redis (59 seconds to be sure it is expires before we cache a new Hash)
    json_string = json.dumps(records)
    client.set("HashValue", json_string, ex=59)

    #Confirmation our data is cached and print out the cache value and expire time
    print(client.get("HashValue"))
    print(client.ttl("HashValue"))
    print("HashValue cached")

    #Timer that makes sure this code is run every minute
    time.sleep(60)
    
#Loop        
while True:
    scraper()