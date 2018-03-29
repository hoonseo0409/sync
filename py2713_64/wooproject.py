# -*- coding: utf-8 -*-

import requests, bs4, json, time


while(1):
    resp = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=BTC-ADA')
    resp.raise_for_status()

    resp.encoding = 'euc-kr'
    html = resp.text

    bs = bs4.BeautifulSoup(html, 'html.parser')

    dictio=json.loads(html)

    print dictio['success']
    if dictio['success']==False:
        print "\a"
    print "\a"
    time.sleep(1)