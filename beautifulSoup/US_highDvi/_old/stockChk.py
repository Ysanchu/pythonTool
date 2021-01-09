#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
import re

def stockChk():
  for num in range(1550 , 1600):
    url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code={}.T".format(num)
    response = requests.get(url)
    # BeautifulSoup設定
    soup = BeautifulSoup(response.text ,"html.parser")
    # 株名
    try :
      stockName = soup.find_all("h1")[0]
    except :
      #print("NG !")
      continue  
    # 株価
    stockPrice = soup.find_all("td" ,class_="stoksPrice")[1]
    print(num , end="\t")
    print(re.sub('<[^>]*?>' , "" , str(stockName)) , end="\t : ")  # タグ消し
    print(re.sub('<[^>]*?>' , "" , str(stockPrice)))  # タグ消し

# Main
if __name__ == "__main__":
  stockChk()
