#!/usr/local/bin/python3

"""
USの株情報から、配当利回りを出すツール
"""

from urllib import request
import lxml.html
import requests
import re
import os,sys

# from lxml import html

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

def filepathChk():
  full_path = "."
  # ファイルパスの存在を確認
  if os.path.exists(full_path):
    print("［" + full_path + "］ は存在します。")
  else:
    print("[" + full_path + "] は存在しません。")
    sys.exit(1)

def fileRead():
  fileName = 'stockTicker.list'
  with open(fileName, mode='r') as readed_file:
    for lineStr in readed_file:
      # 改行コードの削除
      lineStr  = lineStr.rstrip()
      url      = "https://www.bloomberg.co.jp/quote/{}:US".format(lineStr)
      response = requests.get(url)
      # BeautifulSoup設定
      soup = BeautifulSoup(response.text ,"html.parser")
      print(soup)
      print("AAAAAAAAA")
      # XPathで取得したいな。。 urllibならできるらしいだけど。。
      ### title = soup.xpath('//*[@id="content"]/div/div/div[8]/div/div/div[13]/div[2]')
      ### print(title)
      ### print(lineStr)

def urllibChk():
  # ★日本語は文字化けする。対処方法?
  URL      = "https://www.bloomberg.co.jp/quote/T:US"
  data     = request.urlopen(URL)
  raw_html = data.read()
  html     = lxml.html.fromstring(str(raw_html))
  # XPath指定
  title = html.xpath('//*[@id="content"]/div/div/div[8]/div/div/div[13]/div[2]')
  # ------------------------------
  # 色々ためしてみる
  print(title)
  for item in title:
    print(item.tag)

  print(title[0].text)
  # ------------------------------

# Main
if __name__ == "__main__":
  #stockChk()
  #filepathChk()
  #fileRead()
  urllibChk()






# 以下参考
# ============================================================
def test():
  # ★日本語は文字化けする。対処方法?
  URL      = "https://www.bloomberg.co.jp/quote/T:US"
  data     = request.urlopen(URL)
  raw_html = data.read()
  html     = lxml.html.fromstring(str(raw_html))
  # XPath指定
  title = html.xpath('//*[@id="content"]/div/div/div[8]/div/div/div[13]/div[2]')
  # ------------------------------
  # 色々ためしてみる
  print(title)
  # 複数のエレメントがある場合
  for item in title:
    print(item.tag)

  print(title[0].text)
  # ------------------------------
