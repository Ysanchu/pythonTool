#!/usr/local/bin/python3
import requests
from lxml import html
from bs4 import BeautifulSoup

def yamanayTest():
    html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"
    soup = BeautifulSoup(html, "html.parser")

    r = requests.get("https://news.yahoo.co.jp/")
    soup = BeautifulSoup(r.content, "html.parser")
    # ニュース一覧を抽出
    #print(soup.find("ul", "newsFeed_list"))
    #print(soup.select("h2"))

    real_page_tags = soup.find_all("a")
    for tag in real_page_tags:
        print(tag.string)

def nikkeiScraping():
    url = "http://www.nikkei.com/"
    html = requests.get(url)
    #print(html.content)    # html全文
    # BeautifulSourを使用。(初期化)
    soup = BeautifulSoup(html.content , "html.parser")
    #print(soup.title.string)

    ## 書き方で注意するのはclassはPythonでは予約語なのでclass_になります。
    ## 正規表現も使える! ※reをインポート!
    ##  参考:https://qiita.com/itkr/items/513318a9b5b92bd56185
    ##  例)soup.find_all(class_="link", href="/link")
    ##     soup.find_all(attrs={"class": "link", "href": "/link"})
    getStr = soup.find_all("span", class_="k-v")
    for str in getStr:
        print("日経ニュースリスト : {}".format(str.string))

    ## prettifyを呼び出すことできれいに整形して文字列として出力が出来ます。
    #print(soup.prettify)

    ## 保存したブログのボディを表示する際に不要な広告を取り除いたりリンクを新しいタブで開くように
    ##   aタグにtargetを指定したりなどといった使い方をしています

def yahooStockInfoGet():
    # https://stocks.finance.yahoo.co.jp/stocks/detail/?code=XXXX.T
    #                                                         ↑ 銘柄コードがここに入る
    num  = 8591
    url  = ("https://stocks.finance.yahoo.co.jp/stocks/detail/?code={}.T".format(num))
    raw_html = requests.get(url)
    html = lxml.html.fromstring(raw_html.content)
    htmltag = html.xpath
    print(raw_html)


    #soup = BeautifulSoup(raw_html.content , "html.parser")
    #tree = etree.parse("soup")
    #print(tree)
    #AAAA = html.fromstring(str(soup))
    #StockPrice = soup.find_all("td", class_="stoksPrice")
    #print(soup)
    #StockPrice = html.fromstring(str(soup))
    #print(AAAA)


def yahooStockInfoGet_2():
    num  = 8591
    #url  = ("https://stocks.finance.yahoo.co.jp/stocks/detail/?code={}.T".format(num))
    page = requests.get("https://stocks.finance.yahoo.co.jp/stocks/detail/?code={}.T".format(num))
    #page = requests.get("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8591.T")
    print(page)
    tree = html.fromstring(page.content)
    print(tree)
    prePrice = tree.xpath('//*[@id="detail"]/div[2]/div[1]/dl/dd/strong/text()')    
    print('prePrice :', prePrice)
    name = tree.xpath('//*[@id="stockinf"]/div[1]/div[2]/table/tbody/tr/th/h1/text()')
    print('name : ' , name)
    #for num in range(1111,1200):
    #    page = requests.get("https://stocks.finance.yahoo.co.jp/stocks/detail/?code={}.T".format(num))

    
    # //*[@id="stockinf"]/div[1]/div[2]/table/tbody/tr/td[2]

def test():
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.content)
    #This will create a list of prices
    prices = tree.xpath('//span[@class="item-price"]/text()')



# Main
if __name__ == "__main__":
    #yamanayTest()
    #nikkeiScraping()
    #yahooStockInfoGet()
    yahooStockInfoGet_2()
    #test()

