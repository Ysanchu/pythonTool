
🌟pip ソース(tar.gz)のみダウンロード🌟
  # pip download -d src --no-binary :all: openpyxl      # openpyxlソースをダウンロード

■ pip一括Update
  # pip3 list -o | awk 'NR>2{print$1}' | xargs pip3 install -U
    ※ -o : 最新版のパッケージが存在するもののみを出力する

★ Pillow
  画像処理

★ lxml
  XMLやHTMLファイルの処理用ライブラリ
  XPathで使える❗
  https://python.keicode.com/advanced/xml-lxml-1.php

■ openpyxl
  Excelファイル操作方法
  文字列検索とかしてみたいかも
  https://gammasoft.jp/support/how-to-use-openpyxl-for-excel-file/

■ sys
  sysはPythonのインタプリタや実行環境に関する情報を扱うためのライブラリ

■ re
  正規表現

■ shutil
  ファイル操作できる

■ urllib
  urllibはPythonからURLにアクセスしたり、インターネット上のファイルを
  取得したりすることができるパッケージ

■ lxml
  XMLの構文を解析するためのパッケージ

■ subprocess
  引数として与えられたコマンドをただ実行する。
  コマンド実行が成功したら 0 が返る。
  commandsというモジュールもありますが、現在ではメンテナンスが止まっており、
  以降廃止される
  # pip install subprocess.run

■ pexpect
  対話型アプリなどに対して、自動応答できる
  # pip install pexpect

★ pdb
  デバッガ

■ pytube
  Youtubeをダウンロードできる   
  # pip install pytube

■ Tkinter (tkinter)
  GUIアプリ標準のフレームワーク
  少々自由度が足りない。exe化すると少し容量大きい。簡易版
  ttkとは、tkinterの拡張機能のようなもので、いくつか使えるウィジェットが増える
    import tkinter as tk
    import tkinter.ttk as ttk

■ Pyinstaller (pyinstaller)
  Pythonファイルをexe化するライブラリ
  # pip install pyinstaller
    (Macは.appでできる?)

<<注意点>>
  ★ モジュール名とファイル名を一致させない。モジュールではなくファイルから
    インポートしようとする。。
  
<<参考>>
  ・WHLはPython Wheel Packageです。
  
  ・Pythonにはcase文は用意されていません。これは「 if… elif… elif… else 」の
    繰り返しで記述できるためであると公式サイトに説明があります。
    https://docs.python.org/ja/3/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python
  
  ・フォルダパスを指定する時は、rをつけてエスケープシーケンスを無効化するのも忘れずに。
  
  ・Pythonファイルをexe化するライブラリで代表的3つのライブラリ (2021/01/03)
    - Pyinstaller  ← ★ 分かりやすい
    - cx_Freeze    ←   α
    - py2exe
    ※ 初心者には「Pyinstaller」がおすすめです。理由は、exe化する方法が非常にシンプルな点
  
  ・PythonにオススメのGUI
    - Tkinter   ← TkinterはPython標準のGUIフレームワーク (2021/01/03)
    - wxPython  ← α
    - Kivy
    - PyQt
  


