#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import re

## 参考 : https://gammasoft.jp/blog/difference-find-and-select-in-beautiful-soup-of-python/
##Python’s html.parser	“html.parser”  追加ライブラリが不要
##lxml’s HTML parser    “lxml”         高速に処理可
##lxml’s XML parser     “xml”          XMLに対応し、高速に処理可
##html5lib              “html5lib”     正しくHTML5を処理可

## 結果は全てリストで返します。
## soupは 「find , find_all , soup , soup.select」 がある
##  ★ classは予約後の為、注意する

url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8591.T'
response = requests.get(url)
# BeautifulSoup設定
soup = BeautifulSoup(response.text ,"html.parser")
# 株名
stockName = soup.find_all("h1")[0]
print(re.sub('<[^>]*?>' , "" , str(stockName)) , end="\t : ")  # タグ消し
# 株価
stockPrice = soup.find_all("td" ,class_="stoksPrice")[1]
print(re.sub('<[^>]*?>' , "" , str(stockPrice)))  # タグ消し




#### Main
###if __name__ == "__main__":
###    #yamanayTest()
###    #nikkeiScraping()
###    #yahooStockInfoGet()
###    yahooStockInfoGet_2()
###    #test()

