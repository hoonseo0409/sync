from selenium import webdriver
import time
browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://bittrex.com/home/markets")
time.sleep(30.)
browser.quit()
exit()