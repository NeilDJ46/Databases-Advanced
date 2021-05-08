from bs4 import BeautifulSoup
import requests
import pandas as pd
import math
import time
import pymongo as mongo
import redis

client = mongo.MongoClient("mongodb://127.0.0.1:27017")

mh = []
mt = []
mb = []
md = []
r = redis.Redis()


def func(mh, mt, mb, md, col, r):
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    page = requests.get(url)

    url2 = "https://www.coindesk.com/price/bitcoin"
    page2 = requests.get(url2)

    soup = BeautifulSoup(page.content, 'html.parser')
    total = soup.findAll('div', class_='sc-1g6z4xm-0 hXyplo')

    soup2 = BeautifulSoup(page2.content, 'html.parser')
    total2 = soup2.find('div',class_='price-large')
    btcvaluedollar = float(total2.text[1:].replace(',', ''))
    #print(btcvaluedollar)

    #price-large

    hasharray = []
    timearray = []
    btcarray = []
    dollararray = []



    for t in total:
        hashes = t.find('div', class_='sc-1au2w4e-0 bTgHwk')
        time = t.find('div', class_='sc-1au2w4e-0 emaUuf')
        btc = t.find('div', class_='sc-1au2w4e-0 fTyXWG')
        htext = hashes.text[4:len(hashes.text)].strip()
        hasharray.append(htext)
        r.rpush("Hash", str(htext))
        ttext = time.text[4:len(time.text)].strip()
        timearray.append(ttext)
        r.rpush("Time", str(ttext))
        btext = float(btc.text[12:len(btc.text) - 3].strip())
        btcarray.append(btext)
        r.rpush("Bitcoin value", str(btext))
        dtext = btext * btcvaluedollar
        dollararray.append(dtext)
        r.rpush("Dollar value", str(dtext))
        #print(htext)
        #print(ttext)
        #print(btext)
        #print(dtext)
        #print()
    
    r.expire("Hash", 60)
    r.expire("Time", 60)
    r.expire("Bitcoin value", 60)
    r.expire("Dollar value", 60)
    valuedict = {"Hash": hasharray, "Time": timearray, "BTC_value": btcarray, "Dollar_value": dollararray}
    # maxd = max(dollararray)
    # md.append(maxd)
    # index = dollararray.index(maxd)
    # maxhash = hasharray[index]
    # mh.append(maxhash)
    # maxtime = timearray[index]
    # mt.append(maxtime)
    # maxbtc = btcarray[index]
    # mb.append(maxbtc)

    # crypto = {"Hash": maxhash, "Time" : maxtime, "BTC_value" : maxbtc, "Dollar_value" : maxd}

    # col.insert_one(crypto)

    # print("Most Valuable Hash: ", maxhash)
    # print("Time of Hash: ", maxtime)
    # print("BTC Value of Hash: ", maxbtc)
    # print("American Dollar Value of Hash: ", maxd)

    # df = pd.DataFrame(data={"Hash": mh, "Time" : mt, "BTC" : mb, "American Dollar": md})
    # df.to_csv("logfile.txt", header=None, index=None, sep='\t', mode='a')
    # print(df)

db = client["Cryptocurrency"]
col_crypto = db["Crypto"]
#db.Crypto.delete_many({})

while True:
    func(mh, mt, mb, md, col_crypto, r)
    time.sleep(60)