#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,datetime,subprocess

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
sys.path.append('./src/et_xmlfile-1.0.1')
sys.path.append('./src/jdcal-1.4.1')
sys.path.append('./src/openpyxl-3.0.3/')
import openpyxl

__author__  = 'Y.Y'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

DATE_STR    = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
OUTPUT_FILE = 'result_' + DATE_STR + '.txt'
EXE_USER    = 'yamanakayasuyuki'
EXE_HOST    = 'yamanakukinoMBP'

WB          = openpyxl.load_workbook('20200614_pythonTest.xlsx')

#-------------------------------------
# 関数部
#-------------------------------------
def exeUserChk():
    """
    実行ユーザ確認関数
    Args:
        無し
    Returns:
        無し
    Note:
        EXE_USER変数と異なるユーザ名の場合、エラーで終了する。
    """
    # 現在のユーザ名
    exeUser = os.getlogin()
    # ユーザ名確認
    if exeUser != EXE_USER:
        print("現在の実行ユーザが " + exeUser + " です。")
        print("  " + EXE_USER + " ユーザで実行して下さい")
        sys.exit(1)
    
def exeHostChk():
    """
    実行ホスト名確認関数
    Args:
        無し
    Returns:
        無し
    Note:
        EXE_HOST変数と異なるホスト名の場合、エラーで終了する。
    """
    # 現在のホスト名
    exeHost = os.uname()[1]
    # ホスト名確認
    if exeHost != EXE_HOST:
        print("現在の実行ホストが " + exeHost + " です。")
        print("  " + EXE_HOST + " ホストで実行して下さい")
        sys.exit(1)

def howToUse():
    """
    ツールの使い方
    Args:
        無し
    Returns:
        無し
    Note:
    """
    howStr = "使用方法\n"  \
           + "  $ python " + sys.argv[0] + " [-h|--help]\n" 
    print(howStr)

def testInputFunc():
    """
    標準入力テスト関数
    Args:
        無し
    Returns:
        標準入力の結果
    Note:
    """
    #print("読み込みファイル名を入力して下さい\n> ", end="")
    inputStr = input("読み込みファイル名を入力して下さい\n> ")
    print("入力した文字列 : " + str(inputStr))
    return inputStr

def testFileFunc(inputFileName):
    """
    ファイルテスト関数
    Args:
        inputFileName: str
    Returns:
        無し
    Note:
        ファイル読み込み → inputFileNameファイル名を読み込む。
        ファイル書き込み → OUTPUT_FILEのファイル名を作成する。
    """
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

def testFunc():
    """
    テスト関数
    Args:
        無し
    Returns:
        無し
    Note:
    """
    print("testFunc")
    # Shellコマンド実行
    #resCmd = subprocess.check_output("ls -l" , shell=True) ; print(resCmd) # <python2>
    subprocess.run("date" , shell=True, text=True) # <python3>

    sheet = WB['Sheet1']
    for rows in sheet.iter_rows(min_row=1, min_col=1, max_row=20, max_col=20):
        print()
        for cell in rows:
            print(cell.value , end=',')

#-------------------------------------        
# メイン処理
#-------------------------------------
if __name__ == "__main__":
    print(DATE_STR)
    # 実行ホスト名確認関数
    exeUserChk()
    # 実行ユーザ確認関数
    exeHostChk()

    # 引数確認
    if len(sys.argv) == 1:
        # 標準入力テスト関数
        #inputFileName = testInputFunc()
        # ファイルテスト関数
        #testFileFunc(inputFileName)
        # テスト関数
        testFunc()
    elif len(sys.argv) == 2:
        if re.match(r"^-h|^--help", sys.argv[1]):
            # ツールの使い方
            howToUse()
        else:
            print("オプションERROR")
            # 異常終了
            sys.exit(1)
    else:
        # ツールの使い方
        howToUse()
        # 異常終了
        sys.exit(1)

    # 正常終了
    sys.exit(0)

