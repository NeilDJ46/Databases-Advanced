#All import packages that need to be imported
import requests
from bs4 import BeautifulSoup
import time
import threading

# Function that we will loop over every minute
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

    #Open a logfile and print the record with the highest Bitcoin value which sits at position -1 of our records list
    with open("logfile.txt", "a") as logfile:
        print(records[-1], file=logfile)

    #Confirmation our data is printed in the logfile
    print("Logfile updated")

    #Timer that makes sure this code is run every minute
    time.sleep(60)
    
#Loop        
while True:
    scraper()