#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess
import bs4
import requests
import lxml.html

"""
python作成の定型文
Usage :
"""

# 環境定義
#---------------------------
__author__  = 'SANCHU'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

# テスト関数
#---------------------------
def requestsTest():
    print("requestsTest func")
    url      = "https://stocks.finance.yahoo.co.jp/us/ranking/?kd=4&tm=d&mk=&adr=&cg=&idx=&brk=&p=1"
    response = requests.get(url)
    bsObj    = bs4.BeautifulSoup(response.text ,"html.parser")
    # ========================
    ###print(bsObj)
    ###body = bsObj.find('div', attrs={'class': 'post_body'})
    ###print(body)
    ###titles = bsObj.find('div', attrs={'class': 'post_body'}).find_all('h3')
    ###print(titles)
    html = lxml.html.fromstring(str(bsObj))
    # ========================
    #xpathChk = html.xpath('//a')
    xpathChk = html.xpath('//*[@id="main"]/div/table/tbody/tr[2]/td[2]/dl/dd')
    for elem in xpathChk:
        #print(elem.text)
        #print(elem.attrib)
        #print(elem.get('href'))
        elemText  = elem.text
        elemAttr  = elem.attrib
        elemhref  = elem.get('href')
        try:
            print(elemText + "\t" + elemhref)
        except:
            #print("oh.. god")
            continue

# Main
#===========================
if __name__ == "__main__":
    requestsTest()

