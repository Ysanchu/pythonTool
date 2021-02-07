#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
 USの株情報から、配当利回りを出すツール
 2020/05/29 : 別のツールで過去の履歴も参照したいな。
"""
import os
import sys
import re
import datetime
from urllib import request
import lxml.html
import requests

# ログ出力 + 標準出力
# sys.path.append("../..//Fileope/transcript-Make")
sys.path.append(
    "/Users/yamanakayasuyuki/local-work/Mac_tool/python/WORK/Fileope/transcript-Make/")  # noqa
import transcript

# 日本株価参照
# ---------------------------


def usStockChk():
    # 日付取得
    todayStr = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    # ログ + 標準出力開始
    transcript.start('LOG/logfile_' + todayStr + '.log')
    print("ticker\t株価\t配当利回り\t株名")
    print("------------------------------------------------------------")
    # リストファイル指定 & 読み込み
    fileName = 'stockTicker.list'
    with open(fileName, mode='r') as readed_file:
        for lineStr in readed_file:
            # 改行コードの削除
            lineStr = lineStr.rstrip()
            url = "https://www.bloomberg.co.jp/quote/{}:JP".format(lineStr)
            data = request.urlopen(url)
            # スクレイピングした結果が文字化けしてしまったときの解決策
            # https://qiita.com/hibix/items/108911e40f0c27e34da3
            # raw_html = data.read()
            raw_html = data.read().decode(
                data.headers.get_content_charset(), errors='ignore')
            html = lxml.html.fromstring(str(raw_html))
            # 配当利回り取得 (XPath)
            divRate = html.xpath(
                '//*[@id="content"]/div/div/div[8]/div/div/div[13]/div[2]')
            # 株価取得 (XPath)
            price = html.xpath(
                '//*[@id="content"]/div/div/div[1]/div/div[3]/div[2]')
            # 株名 (日本語文字化けする。。どうにかできないか。。)
            name = html.xpath(
                '//*[@id="content"]/div/div/div[1]/div/h1')
            # 株価・配当を出力
            print(lineStr + "\t" + price[0].text + "\t" +
                  divRate[0].text + "\t" + name[0].text)
    # ログ出力終了
    transcript.stop()


# Main
# ===========================
if __name__ == "__main__":
    usStockChk()
