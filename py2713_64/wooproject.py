# -*- coding: utf-8 -*-

import requests, bs4, json
import ast

resp = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=BTC-ADA')
resp.raise_for_status()

resp.encoding = 'euc-kr'
html = resp.text

bs = bs4.BeautifulSoup(html, 'html.parser')
tags = bs.select('success')  # Top 뉴스
#title = tags.getText()
print(html)
#dict= ast.literal_eval(html)
dict=json.loads(html)
print dict