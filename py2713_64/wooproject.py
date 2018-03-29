# -*- coding: utf-8 -*-

import requests, bs4, json, time, csv, io, time, urlparse

import winsound

from flask import request

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
        resp=requests.get(coin)
        #test = self.request.get('market', default = '*', type=str)
        parsed = urlparse.urlparse(coin)
        print urlparse.parse_qs(parsed.query)['market'][0]
        resp.raise_for_status()
        resp.encoding = 'euc-kr'
        html = resp.text
        #bs = bs4.BeautifulSoup(html, 'html.parser')
        dictio=json.loads(html)
        print dictio['success']
        if dictio['success']==True:
            start=time.time()
            while(1):
                winsound.Beep(frequency, duration)
                print('%d초 시간이 지났습니다.')%(time.time()-start)


