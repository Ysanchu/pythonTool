#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,datetime,subprocess
from pytube import YouTube

"""
■ 概要
  python作成の定型文

■ 使用方法
■ 補足
■ 改版履歴
  YYYY-MM-DD 1.0.0  Y.Y    新規作成
"""

#-------------------------------------
# 定義部
#-------------------------------------
__author__  = 'Y.Y'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

DATE_STR    = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
OUTPUT_FILE = 'result_' + DATE_STR + '.txt'
EXE_USER    = 'yamanakayasuyuki'
EXE_HOST    = 'yamanakukinoMBP'

#-------------------------------------
# 関数部
#-------------------------------------
## 実行ユーザ確認関数
def exeUserChk():
    # 現在のユーザ名
    exeUser = os.getlogin()
    # ユーザ名確認
    if exeUser != EXE_USER:
        print("現在の実行ユーザが " + exeUser + " です。")
        print("  " + EXE_USER + " ユーザで実行して下さい")
        sys.exit(1)
    
## 実行ホスト名確認関数
def exeHostChk():
    # 現在のホスト名
    exeHost = os.uname()[1]
    # ホスト名確認
    if exeHost != EXE_HOST:
        print("現在の実行ホストが " + exeHost + " です。")
        print("  " + EXE_HOST + " ホストで実行して下さい")
        sys.exit(1)

## 標準入力テスト関数
def testInputFunc():
    print("読み込みファイル名を入力して下さい\n> ", end="")
    inputStr = input()
    print("入力した文字列 : " + str(inputStr))
    return inputStr

## ファイルテスト関数
def testFileFunc(inputFileName):
    # ファイルの存在確認
    #   os.path.exists(Str) : Dir & File
    #   os.path.isdir(Str)  : Dir
    if (os.path.isfile(inputFileName)):
        print("ファイルを読み込みます。[" + inputFileName + "]")
        try:
            # ファイルオープン
            with open(inputFileName,"r") as file:
                # 1行ずつ読み込み
                for lineStr in file:
                    # 先頭、末尾の空白文字列削除
                    lineStr = lineStr.strip()
                    # 標準出力
                    print(lineStr)
        except Exception as errMsg:
            print("ファイルは存在しましたが、読み込みエラーが発生しました。")
    else:
        print("読み込みファイルが存在しませんでした。[" + inputFileName + "]")

    # ファイル書き込み(test用)
    outputFile = open(OUTPUT_FILE, "w")
    outputFile.write("test " + DATE_STR)

## テスト関数
def testFunc():
    print("testFunc")
    url = 'https://www.youtube.com/watch?v=ePoRyZMtyUU'
    YouTube(url).streams.first().download(r"./" , "output")

def inputDownload():
    print("inputDownload") 
    url = input("ダウンロードしたい動画のURL\n> ")
    print(*YouTube(url).streams.all(), sep="\n")
    itag = int(input("ダウンロードしたい動画のタグ:"))
    YouTube(url).streams.get_by_itag(itag).download(r"./", "output")

#-------------------------------------        
# メイン処理
#-------------------------------------
if __name__ == "__main__":
    print(DATE_STR)
    exeUserChk()
    exeHostChk()
    #inputFileName = testInputFunc()
    #testFileFunc(inputFileName)
    #testFunc()
    inputDownload()

