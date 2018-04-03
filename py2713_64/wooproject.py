# -*- coding: utf-8 -*-

import requests, bs4, json, time, csv, io, time, urlparse, pygame


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#from flask import request

frequency = 2000  # Set Frequency To 2500 Hertz
duration = 2000  # Set Duration To 1000 ms == 1 second





f = io.open('sj.csv', 'r', encoding='utf-8-sig')
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

#test=['UPBIT', 'KRW']
round=0

present=time.time()

while(1):
    
    """
    print len(coinlist)

    print ('{} rounds was done'.format(round))
    round=round+1
    """



    headers = {'User-Agent': 'firefox'}

    time.sleep(1.)
    resp=requests.get('https://bittrex.com/api/v1.1/public/getcurrencies', headers=headers)

    #resp.raise_for_status()
    #resp.encoding = 'euc-kr'
    resp.encoding = 'utf-8-sig'

    html = resp.text
    print html
    print '----------------------------------------------------'

    for coin in coinlist:
        if coin in html:
            alarm = 1
            #parsed = urlparse.urlparse(coin)
            find_dict[coin] = time.time()
            coinlist.remove(coin)
            break

    if alarm == 1 and int(present - time.time()) % 5 == 0:
        bang.play()
        for name, thattime in find_dict.items():
            print ('{} 의 상장을 탐지한지 {}초 경과되었습니다.'.format(name, time.time() - thattime))

        #dictio=json.loads(html)

        #print dictio['success']

        """
        if dictio['success']==False:
            alarm=1
            parsed = urlparse.urlparse(coin)
            find_dict[urlparse.parse_qs(parsed.query)['market'][0][4:]]=time.time()
            coinlist.remove(coin)
        """

