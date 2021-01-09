#!/usr/local/bin/python3

#import requests
#from lxml import html
#from bs4 import BeautifulSoup
import requests
import lxml.html

def yamanayTest():
    # WebサイトのURLを指定
    url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8591.T"
    # Requestsを利用してWebページを取得する
    r = requests.get(url)
    # lxmlを利用してWebページを解析する
    html = lxml.html.fromstring(r.text)
    # lxmlのfindallを利用して、ヘッドラインのタイトルを取得する
    #elems = html.findall(".//a[@class='ipQwMb Q7tWef']//span")
    elems = html.findall('.//*[@id="stockinf"]/div[1]/div[2]/table/tbody/tr/')
    elems = html.xpath('//*[@id="stockinf"]/div[1]/div[2]/table/tbody/tr/')
    for elem in elems:
        #print(elem.text_content)
        print(elem.text)

# Main
if __name__ == "__main__":
    yamanayTest()
