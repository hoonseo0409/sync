# -*- coding: utf-8 -*-

import requests, bs4, json, time, csv, io

import winsound
frequency = 500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

f = io.open('coinlist.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
coinlist=[]
for line in rdr:
    coinlist.append(line[0])
print coinlist
f.close()


while(1):
    i=0
    for coin in coinlist:
        #resp = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=BTC-ADA')
        resp=requests.get(coin)
        resp.raise_for_status()
        resp.encoding = 'euc-kr'
        html = resp.text
        #bs = bs4.BeautifulSoup(html, 'html.parser')
        dictio=json.loads(html)
        print i
        i=i+1
        print dictio['success']
        if dictio['success']==True:
            winsound.Beep(frequency, duration)

