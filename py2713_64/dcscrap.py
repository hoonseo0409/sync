import scrapy
import time

headers = {'User-Agent': 'firefox'}
request = scrapy.Request('http://bithumb.cafe/notice', headers=headers, encoding='utf-8-sig')
print response.xpath()