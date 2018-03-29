# -*- coding: utf-8 -*-

import requests, bs4, json, time

import winsound
frequency = 1000  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second




while(1):
    resp = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=BTC-ADA')
    resp.raise_for_status()

    resp.encoding = 'euc-kr'
    html = resp.text

    bs = bs4.BeautifulSoup(html, 'html.parser')

    dictio=json.loads(html)

    print dictio['success']
    if dictio['success']==True:
        print '\a'
        winsound.Beep(frequency, duration)

    time.sleep(1)