# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait

import pygame
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://bittrex.com/home/markets")
time.sleep(30.)
browser.quit()
exit()
"""

pygame.mixer.init()
bang=pygame.mixer.Sound("Alarm05.wav")
round=0
#present=time.time()
alarm=0
find_dict={}

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("http://bithumb.cafe/notice")
#html = driver.page_source
#soup = BeautifulSoup(html, 'html.parser')
before = driver.find_element_by_xpath('//*[@id="primary-fullwidth"]/article[1]/h3/a').text


while(1):
    print '{} 번 페이지를 요청하였습니다.'.format(round)

    driver.get("http://bithumb.cafe/notice")
    now = driver.find_element_by_xpath('//*[@id="primary-fullwidth"]/article[1]/h3/a').text

    if alarm == 1:
        bang.play()
        for name, thattime in find_dict.items():
            print ('{} 의 상장을 탐지한지 {}초 경과되었습니다.'.format(name, int(time.time() - thattime)))


    if now != before and ('상장' in now):
        alarm=1
        find_dict[now] = time.time()
        before=now
    elif now != before:
        before = now

    round = round +1
    time.sleep(3.)

    if '상장' in now:
        print now




#print driver.page_source