# -*- coding: utf-8 -*-

import csv
import subprocess
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import settings
import threading
import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import random
import datetime
from binance.client import Client
import telegram

reload(sys)
sys.setdefaultencoding('utf-8')

trade_number=0
trade_history={}

client = Client(settings.APIKEY, settings.SECRET)
kill=0

marketpt = 0.01 #투자 비중의 기본값
waitforselling = 1 # 매수후 절반을 매도하기까지 기다리는 시간 단위는 초
# limitpt=0.001

my_token = settings.my_token
bot = telegram.Bot(token=my_token)  # bot을 선언합니다.
chat_id = settings.chat_id  # 각자 id 기입


def findin_notice_bithumb():
    epoch = 1
    driver = webdriver.Chrome("C:\chromedriver.exe")
    driver.get("http://bithumb.cafe/notice")
    driver.implicitly_wait(60)
    before = driver.find_element_by_xpath('//*[@id="primary-fullwidth"]/article[1]/h3/a').text

    while (1):
        try:
            if epoch%10 == 1:
                print '빗썸 공지사항에서 {} 번 페이지를 요청하였습니다.'.format(epoch)
            driver.get("http://bithumb.cafe/notice")
            driver.implicitly_wait(60)
            now = driver.find_element_by_xpath('//*[@id="primary-fullwidth"]/article[1]/h3/a').text


            if now == before or ('상장' not in now):
                may_lst=[]
                avoid = ['PRO', 'API', 'BTC', 'USD', 'KRW', 'KST', 'MTS', 'FAQ', 'QNA', 'SMS']

                upper=''
                for i in now:
                    if i.isupper():
                        length = length + 1
                        upper = upper + i
                    elif len(upper)>= 3 and (upper not in avoid):
                        may_lst.append(upper)
                        length = 0
                        upper = ''
                    else:
                        length = 0
                        upper = ''

                driver.find_element_by_xpath('//*[@id="primary-fullwidth"]/article[1]/h3/a').click()
                driver.implicitly_wait(60)
                print(driver.find_element_by_xpath('//*[@id="primary-left"]/article/div').text)

                for i in driver.find_element_by_xpath('//*[@id="primary-left"]/article/div').text:
                    if i.isupper():
                        length = length + 1
                        upper = upper + i
                    elif len(upper)>= 3 and (upper not in avoid):
                        may_lst.append(upper)
                        length = 0
                        upper = ''
                    else:
                        length = 0
                        upper = ''

                may_lst = list(set(may_lst))

                j=0
                for j in range (len(may_lst)):
                    may_lst[j]=may_lst[j].encode('utf-8')
                print may_lst

            before=now
            epoch = epoch + 1
            time.sleep(random.randrange(3, 20))
        except Exception as ex:
            time.sleep(random.randrange(3, 20))


findin_notice_bithumb()