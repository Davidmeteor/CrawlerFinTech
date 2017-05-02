import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class FinTechCrawler(scrapy.Spider):
    name = 'fintech'
    start_urls = ['http://www.sitca.org.tw/ROC/Industry/IN3201.aspx']
    driver = webdriver.Chrome('/Users/david/Project/Crawler/chromedriver') 
    driver.get(start_urls[0])    
    time.sleep(5)
    # press the query button
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnQuery").click()
    # load the page after sending the query request
    pagesource = driver.page_source
    print "test"
    print(pagesource)

    #def parse(self, response):
        #res = BeautifulSoup(response.body)
        #print "test"
        #print res
        #return
