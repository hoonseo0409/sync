from selenium import webdriver
from bs4 import BeautifulSoup

import time
"""
browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://bittrex.com/home/markets")
time.sleep(30.)
browser.quit()
exit()
"""

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("http://bithumb.cafe/notice")
#html = driver.page_source
#soup = BeautifulSoup(html, 'html.parser')

p_element = driver.find_element_by_xpath('//*[@id="primary-fullwidth"]/article[1]/h3/a')
print p_element.text


#print driver.page_source