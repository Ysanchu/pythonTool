#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
 ■ 概要
   python作成の定型文
 
 ■ 使用方法
   # python pythonInit.py
   
 ■ 補足
   - Support: python 3.8 
   - [# noqa] コメントはVScode自動整形無効対象
   - [命名規則] によると、ファイル名は大文字は使わない

 ■ 改版履歴
   YYYY-MM-DD 1.0.0  Y.Y    新規作成
"""

# -------------------------------------
# 定義部
# -------------------------------------
import sys
import os
import re
import csv
import pwd
import datetime
import subprocess
import logging
import time

import pyautogui
import pyperclip  # クリップボードへのコピーで使用
import tkinter    # GUI

__author__ = 'Y.Y'
__version__ = '1.0.0'
__date__ = 'YYYY/MM/DD'

DATE_STR = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
OUTPUT_FILE = 'result_' + DATE_STR + '.txt'
EXE_USER = 'yamanakayasuyuki'
EXE_HOST = 'yamanakukinoMBP'
LOG_FILE = 'exampleLog.txt'

# ロギング設定
# <出力例> : 2021-01-10 00:45:08.134 <DEBUG> yamanakayasuyuki - MainProcess-13882 test_exe_func() XXXXX [pythonInit.py:175]
# logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
#                     format='%(asctime)s.%(msecs)-03d <%(levelname)s> {0} - %(processName)s-%(process)d %(funcName)s() %(message)s [%(pathname)s:%(lineno)s]'.format(
#                         os.getlogin()),
#                     datefmt='%Y-%m-%d %H:%M:%S')

# -------------------------------------
# 関数部
# -------------------------------------


def user_chk():
    """
    実行ユーザ確認

    Args:
        無し
    Returns:
        無し
    Note:
        EXE_USER変数と異なるユーザ名の場合、エラーで終了する。
    """
    # 現在のユーザ名
    exe_user_now = os.getlogin()
    # ユーザ名確認
    if exe_user_now != EXE_USER:
        print("現在の実行ユーザが " + exe_user_now + " です。")
        print("  " + EXE_USER + " ユーザで実行して下さい")
        sys.exit(1)


def host_chk():
    """
    実行ホスト名確認

    Args:
        無し
    Returns:
        無し
    Note:
        EXE_HOST変数と異なるホスト名の場合、エラーで終了する。
    """
    # 現在のホスト名
    exe_host_now = os.uname()[1]
    # ホスト名確認
    if exe_host_now != EXE_HOST:
        print("現在の実行ホストが " + exe_host_now + " です。")
        print("  " + EXE_HOST + " ホストで実行して下さい")
        sys.exit(1)


def how_to_use():
    """
    ツールの使い方標準出力

    Args:
        無し
    Returns:
        無し
    Note:
    """
    how_str = "使用方法\n"  \
        + "  $ python " + sys.argv[0] + " [-h|--help]\n"
    print(how_str)


def test_input_finc():
    """
    標準入力テスト関数

    Args:
        無し
    Returns:
        標準入力の結果
    Note:
    """
    #print("読み込みファイル名を入力して下さい\n> ", end="")
    input_str = input("読み込みファイル名を入力して下さい\n> ")
    print("入力した文字列 : " + str(input_str))
    return input_str


def test_file_func(input_file):
    """
    ファイルテスト関数

    Args:
        input_file: str
    Returns:
        無し
    Note:
        ファイル読み込み → input_fileファイル名を読み込む。
        ファイル書き込み → OUTPUT_FILEのファイル名を作成する。
    """
    # ファイルの存在確認
    #   os.path.exists(Str) : Dir & File
    #   os.path.isdir(Str)  : Dir
    if (os.path.isfile(input_file)):
        print("ファイルを読み込みます。[" + input_file + "]")
        try:
            # ファイルオープン
            with open(input_file, "r") as file:
                # 1行ずつ読み込み
                for line_str in file:
                    # 先頭、末尾の空白文字列削除
                    line_str = line_str.strip()
                    # 標準出力
                    print(line_str)
        except Exception as err_msg:
            print("ファイルは存在しましたが、読み込みエラーが発生しました。")
    else:
        print("読み込みファイルが存在しませんでした。[" + input_file + "]")

    # ファイル書き込み(test用)
    output_file = open(OUTPUT_FILE, "w")
    output_file.write("test " + DATE_STR)


def test_exe_func():
    """
    テスト関数

    Args:
        無し
    Returns:
        無し
    Note:
        マウスクリック、連射設定、場所の指定以外にクリック数、クリック間隔、ボタンの指定ができる
        # pyautogui.click(x,y, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
        文字列入力。interval=0.25だと人が入力している速度に近づく
        # pyautogui.write('dictionary_', interval=0.25)
    """
    print("test_exe_func")
    # logging.debug('Start')
    # Shellコマンド実行
    # subprocess.call("ls -l" , shell=True)        # <python2>
    subprocess.run("date", shell=True, text=True)  # <python3>

    # pyautogui.confirm(text='google辞書を開きます。よろしいですか？',
    #                  title='check', buttons=['OK', 'Cancel'], timeout=3)

    print("google辞書を開きます")
    pyautogui.click(985, 13, interval=1)
    pyautogui.click(1039, 294, interval=3)
    print("google辞書のExportを実行します")
    pyautogui.click(361, 219, interval=1)
    pyautogui.click(406, 397, interval=2)
    # メッセージボックスクリック
    pyautogui.click(561, 213, interval=1)

    # dictionary_YY-MM-DD.txt作成
    # #Try1: アンダーバーが打てなかった。。USキーボードが関係している。。
    #      「 _ 」 → 「 = 」
    #      「 \'」 → 「 - 」
    # # #pyautogui.press("kana")
    # #pyautogui.hotkey('ctrl', 'space')
    # #pyautogui.write('dictionary_')
    # #Try2: import pyperclip  で対応
    # #       → google辞書Exportでは、「command + V」が効かなかった。。
    # #pyperclip.copy('dictionary_')
    # pyautogui.hotkey('command', 'v')  # 貼り付け
    # Try3: 辞書登録してやる！(最終手段！)

    # かな → 英字変換
    pyautogui.press("kana", interval=0.3)
    pyautogui.hotkey('ctrl', 'space')
    pyautogui.write('dictionary')
    pyautogui.press("kana")
    pyautogui.write('annda-ba-')
    pyautogui.press('space', presses=1, interval=0.5)
    pyautogui.press('Enter')

    # 今日の日付を入力 (google辞書活用。YYYY-MM-DD形式)
    pyautogui.press("kana")
    pyautogui.write('kyou')
    pyautogui.press('space', presses=5, interval=0.5)
    pyautogui.press('Enter')

    # 保存
    pyautogui.click(799, 349, interval=1)

    # 「辞書のエクスポートが完了しました」メッセージOK
    # pyautogui.click(733, 422, clicks=2, interval=0.3)
    pyautogui.moveTo(733, 422)
    # pyautogui.doubleClick()
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')

    print("google辞書を終了します")
    pyautogui.hotkey('command', 'q', interval=1)

    print("ターミナルを開きます")
    # pyautogui.hotkey('fn', 'f4') これが使えなかった。。 (fnキーが効かない用に見える)
    # ダッシュボード → コマンドプロンプト起動
    pyautogui.moveTo(1279, 116)
    time.sleep(1)
    pyautogui.click(1261, 117, interval=1)
    pyautogui.hotkey('command', 'n', interval=0.5)

    # ターミナル操作(コマンド実行)
    print("コマンド実行")
    pyperclip.copy(
        '/bin/bash /Users/yamanakayasuyuki/local-work/Mac_tool/bash/_googleZipMake.sh')
    pyautogui.hotkey('command', 'v')  # 貼り付け
    pyautogui.press('Enter', interval=0.5)
    pyperclip.copy(
        'pushd /Users/yamanakayasuyuki/Git/templete ; /bin/bash _update.sh ; popd')
    pyautogui.hotkey('command', 'v')  # 貼り付け
    pyautogui.press('Enter', interval=10)

    print("ターミナルを終了します")
    pyautogui.hotkey('command', 'w')

    print("処理を終了します")
    # logging.debug('End')


# -------------------------------------
# メイン処理
# -------------------------------------
if __name__ == "__main__":
    print(DATE_STR)
    # logging.debug('pythonInit.py Start')

    # 実行ホスト名確認関数
    user_chk()
    # 実行ユーザ確認関数
    host_chk()

    # 引数確認
    if len(sys.argv) == 1:
        # 標準入力テスト関数
        # input_file = test_input_finc()
        # ファイルテスト関数
        # test_file_func(input_file)
        # テスト関数
        test_exe_func()
    elif len(sys.argv) == 2:
        if re.match(r"^-h|^--help", sys.argv[1]):
            # ツールの使い方
            how_to_use()
        else:
            print("オプションERROR")
            # 異常終了
            sys.exit(1)
    else:
        # ツールの使い方
        how_to_use()
        # 異常終了
        sys.exit(1)

    # 正常終了
    # logging.debug('pythonInit.py End')
    sys.exit(0)
