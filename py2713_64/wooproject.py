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
listed_coin_lst=[]
headers = {'User-Agent': 'firefox'}
round=0
present=time.time()

while(1):
    print '{} 번 페이지를 요청하였습니다.'.format(round)
    resp=requests.get('http://bithumb.cafe/notice', headers=headers)
    resp.encoding = 'utf-8-sig'
    html = resp.text

    print html
    time.sleep(15.)

    dictio = json.loads(html)

    print dictio
    """
    result=dictio['result']
    
    
    for listed_coin in result:
        listed_coin_lst.append(listed_coin['Currency'])
    #print listed_coin_lst

    for coin in coinlist:
        if coin in listed_coin_lst:
            alarm = 1
            # parsed = urlparse.urlparse(coin)
            find_dict[coin] = time.time()
            coinlist.remove(coin)

    if alarm == 1 and int(present - time.time()) % 3 == 0:
        bang.play()
        for name, thattime in find_dict.items():
            print ('{} 의 상장을 탐지한지 {}초 경과되었습니다.'.format(name, int(time.time() - thattime)))

    time.sleep(1.)
    round=round +1
    
    """

    """
    for coin in coinlist:
        tick=tick+1

        if alarm==1 and tick%10==0:
            bang.play()
            for name, thattime in find_dict.items():
                print ('{} 의 상장을 탐지한지 {}초 경과되었습니다.'.format(name, time.time()-thattime))

        resp=requests.get(coin)

        resp.raise_for_status()
        resp.encoding = 'euc-kr'
        html = resp.text
        dictio=json.loads(html)

        #print dictio['success']
        print (len(coinlist))

        if dictio['success']==False:
            alarm=1
            parsed = urlparse.urlparse(coin)
            find_dict[urlparse.parse_qs(parsed.query)['market'][0][4:]]=time.time()
            coinlist.remove(coin)
    """

