# -*- coding: utf-8 -*-

import requests, bs4, json, time, csv, io, time, urlparse, pygame



#from flask import request

frequency = 2000  # Set Frequency To 2500 Hertz
duration = 2000  # Set Duration To 1000 ms == 1 second





f = io.open('coinlist.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
coinlist=[]
for line in rdr:
    coinlist.append(line[0])
print coinlist
f.close()


while(1):

    for coin in coinlist:
        resp=requests.get(coin)

        resp.raise_for_status()
        resp.encoding = 'euc-kr'
        html = resp.text
        #bs = bs4.BeautifulSoup(html, 'html.parser')
        dictio=json.loads(html)

        print dictio['success']
        
        if dictio['success']==False:
            start=time.time()
            while(1):
                pygame.mixer.init()
                bang=pygame.mixer.Sound("Alarm05.wav")
                parsed = urlparse.urlparse(coin)
                print ('%s 가 상장된 것을 감지한지 %d초가 경과하였습니다.')%(urlparse.parse_qs(parsed.query)['market'][0][4:],(time.time()-start))
                bang.play()
                time.sleep(2)