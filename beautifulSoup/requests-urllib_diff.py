#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess
import bs4
import requests
import urllib

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
    url      = "https://kaiten-heiten.com/heiten/heiten-gyousyubetsu/"
    response = requests.get(url)
    bsObj    = bs4.BeautifulSoup(response.text ,"html.parser")
    print(bsObj)

def urllibTest():
    print("urllibTest func");
    url      = "https://kaiten-heiten.com/heiten/heiten-gyousyubetsu/"
    html     = urllib.request.urlopen(url)
    bsObj    = bs4.BeautifulSoup(html, 'html.parser')
    print(bsObj)

# Main
#===========================
if __name__ == "__main__":
    #requestsTest()
    urllibTest()

