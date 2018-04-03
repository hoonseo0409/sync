# -*- coding: utf-8 -*-

import requests, bs4, json, time, csv, io, time, urlparse, pygame


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#from flask import request

frequency = 2000  # Set Frequency To 2500 Hertz
duration = 2000  # Set Duration To 1000 ms == 1 second





f = io.open('upbit_url.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)

coinlist=[]
for line in rdr:
    coinlist.append(line[0])
print (coinlist)
f.close()

find_dict={}
alarm=0
tick=1
pygame.mixer.init()
bang=pygame.mixer.Sound("Alarm05.wav")

test=['UPBIT', 'KRW']
round=0

listed_coin_lst=[]

while(1):
    
    
    print len(coinlist)

    print ('{} rounds was done'.format(round))
    round=round+1


    for coin in coinlist:
        tick=tick+1

        if alarm==1 and tick%100==0:
            bang.play()
            for name, thattime in find_dict.items():
                print ('{} 의 상장을 탐지한지 {}초 경과되었습니다.'.format(name, time.time()-thattime))

        headers = {'User-Agent': 'firefox'}

        #time.sleep(0.2)
        resp=requests.get(coin, headers=headers)

        #resp.raise_for_status()
        #resp.encoding = 'euc-kr'
        resp.encoding = 'utf-8-sig'

        html = resp.text



        for elem in test:
            if elem in html:
                alarm = 1
                parsed = urlparse.urlparse(coin)
                find_dict[urlparse.parse_qs(parsed.query)['code'][0][15:]] = time.time()
                coinlist.remove(coin)
                break



        #dictio=json.loads(html)

        #print dictio['success']

        """
        if dictio['success']==False:
            alarm=1
            parsed = urlparse.urlparse(coin)
            find_dict[urlparse.parse_qs(parsed.query)['market'][0][4:]]=time.time()
            coinlist.remove(coin)
        """

