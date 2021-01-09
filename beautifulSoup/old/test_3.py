#!/usr/local/bin/python3
import requests
import lxml.html

def yamanayTest():
    r = requests.get("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8591.T")
    html = r.text
    root = lxml.html.fromstring(html)
    titleH1 = root.xpath('//*[@id="stockinf"]/div[1]/div[2]/table/node()')
    print(titleH1)
    #print(titleH1[0].text)

def yamanayTest_2():
    #target_url = 'http://news.tv-asahi.co.jp/news_politics/articles/000041338.html'
    target_url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8591.T"
    target_html = requests.get(target_url).text
    root = lxml.html.fromstring(target_html)
    #text_content()メソッドはそのタグ以下にあるすべてのテキストを取得する
    #root.cssselect('#news_body > p').text_content()
    #print(root.cssselect('#news_body > p').text_content())
    print(root.cssselect('#stockinf > div.stocksDtl.clearFix > div.forAddPortfolio > table > tbody > tr > th > h1'))
    

# Main
if __name__ == "__main__":
    #yamanayTest()
    yamanayTest_2()