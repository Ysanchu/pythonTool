#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,datetime,subprocess
import tkinter as tk
import tkinter.ttk as ttk

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
    #subprocess.run("date" , shell=True, text=True)

    #root = tk.Tk()
    #button = tk.Button(root, text = 'Hello, Python3/Tkinter!!')
    #button.pack()
    #root.mainloop()

    # メインウィンドウ生成
    root = tk.Tk()
    # ウィンドウタイトルを指定
    root.title("Image editing app")
    # ウィンドウサイズを指定
    #root.geometry("400x550")
    root.geometry("600x600")
    # ウィンドウサイズの変更可否設定
    root.resizable(0,0)
    # ウィンドウの背景色
    #root.configure(bg="white")
    root.configure(bg="#CCFFFF")

    ### この下に描画内容を書く ###
    wrpFrm = tk.Frame(root)
    wrpFrm.configure(bg="white")
    wrpFrm.pack(padx=3, pady=3, fill="both", expand=1)

    # 読み込んだ画像リスト
    imgList = ttk.Treeview(wrpFrm)
    imgList.configure(column=(1,2), show="headings", height=6)
    imgList.column(1, width=30)
    imgList.column(2, width=361)
    imgList.heading(1, text="No")
    imgList.heading(2, text="path/name")
    imgList.pack()

    # ボタン中央揃え用のフレーム
    btnFrm = tk.Frame(wrpFrm)
    btnFrm.configure(bg="white")
    btnFrm.pack(pady=5)

    # 画像追加ボタン
    addBtn = tk.Button(btnFrm)
    addBtn.configure(text="画像を追加")
    addBtn.pack(side="left", padx=5)

    # 画像リセットボタン
    resetBtn = tk.Button(btnFrm)
    resetBtn.configure(text="画像をリセット")
    resetBtn.pack(side="left", padx=5)

    # グリッド用のFrame
    confGridFrm = tk.Frame(wrpFrm)
    confGridFrm.configure(bg="white")
    confGridFrm.pack(padx=3, pady=3, fill="x")

    # チェックボックス設置
    renameChkVar = tk.BooleanVar()
    renameChkVar.set(True)
    renameChk = tk.Checkbutton(confGridFrm)
    renameChk.configure(
        text="リネームする",
        variable=renameChkVar,
        bg="white")
    renameChk.grid(row=0, column=0, sticky="nw")

    # ネームルールフレーム
    renameFrm = tk.LabelFrame(confGridFrm)
    renameFrm.configure(bg="white", text="リネームルール", relief="groove")
    renameFrm.grid(row=0, column=1, pady=(0,5))

    # レイアウト用のFrame
    renameFrmInn = tk.Frame(renameFrm)
    renameFrmInn.configure(bg="white")
    renameFrmInn.pack(padx=8, pady=(0,5))

    # ファイル名
    fNameLbl = tk.Label(renameFrmInn)
    fNameLbl.configure(text="ファイル名", bg="white")
    fNameLbl.grid(row=0, column=0, sticky="nw")

    # ファイル名入力欄
    fNameEnt = tk.Entry(renameFrmInn)
    fNameEnt.insert("end", "img")
    fNameEnt.grid(row=0, column=1, pady=(0,2), sticky="w")

    # 開始番号
    fNumLbl = tk.Label(renameFrmInn, text="開始番号")
    fNumLbl.configure(bg="white")
    fNumLbl.grid(row=1, column=0, sticky="w")

    # 開始番号入力欄
    fNumEnt = tk.Entry(renameFrmInn, width=10)
    fNumEnt.insert("end", "1")
    fNumEnt.grid(row=1, column=1, sticky="w")

    # アンダーバーチェック
    usChkVar = tk.BooleanVar()
    usChkVar.set(True)
    usChk = tk.Checkbutton(renameFrmInn)
    usChk.configure(
        bg="white",
        text="区切り文字にアンダースコア(_)を使用する",
        variable=usChkVar)
    usChk.grid(row=2, column=0, columnspan=2, sticky="nw")

    # 出力結果タイトル
    nResLbl = tk.Label(renameFrmInn)
    nResLbl.configure(bg="white", text="出力結果例")
    nResLbl.grid(row=3, column=0, sticky="w")

    # 出力結果
    nResOut = tk.Label(renameFrmInn)
    nResOut.configure(bg="white", text="img_1.png")
    nResOut.grid(row=3, column=1, sticky="w")

    # リサイズチェック
    resizeChkVar = tk.BooleanVar()
    resizeChkVar.set(True)
    resizeChk = tk.Checkbutton(confGridFrm)
    resizeChk.configure(
        bg="white",
        text="幅を固定値でリサイズ",
        variable=resizeChkVar)
    resizeChk.grid(row=3, column=0, padx=(0,15), sticky="nw")

    # リサイズ幅設定フレーム
    resizeFrm = tk.Frame(confGridFrm)
    resizeFrm.configure(bg="white")
    resizeFrm.grid(row=3, column=1, sticky="nw", pady=(0,5))

    # "幅"
    resizeLbl1 = tk.Label(resizeFrm)
    resizeLbl1.configure(bg="white", text="幅")
    resizeLbl1.pack(side="left")

    # 幅指定入力欄
    resizeEnt = tk.Entry(resizeFrm)
    resizeEnt.configure(width=10, relief="groove")
    resizeEnt.insert("end", "600")
    resizeEnt.pack(side="left", padx=(15,0))

    # "px"
    resizeLbl2 = tk.Label(resizeFrm)
    resizeLbl2.configure(bg="white", text="px")
    resizeLbl2.pack(side="left")

    # 拡張子指定タイトル
    extTtlLbl = tk.Label(confGridFrm)
    extTtlLbl.configure(bg="white", text="拡張子を指定")
    extTtlLbl.grid(row=4, column=0, sticky="nw")

    # 拡張子フレーム
    extFrm = tk.Frame(confGridFrm)
    extFrm.configure(bg="white")
    extFrm.grid(row=4, column=1, sticky="nw", pady=(0,5))

    # "形式"
    extLbl = tk.Label(extFrm)
    extLbl.configure(bg="white", text="形式")
    extLbl.pack(side="left")

    # 拡張子セレクト
    extSelect = ttk.Combobox(extFrm)
    extSelect.configure(
        state="readonly",
        width=8,
        value = ("png", "jpeg"))
    extSelect.current(0)
    extSelect.pack(side="left", padx=(3,0))

    # 保存先タイトル
    acvTtlLbl = tk.Label(confGridFrm)
    acvTtlLbl.configure(bg="white", text="保存先を選択")
    acvTtlLbl.grid(row=5, column=0, sticky="nw")

    # 保存先フレーム
    acvFrm = tk.Frame(confGridFrm)
    acvFrm.configure(bg="white")
    acvFrm.grid(row=5, column=1, sticky="nw", pady=(0,5))

    # 保存先テキスト
    acvLbl = tk.Label(acvFrm)
    acvLbl.configure(text="未選択")
    acvLbl.pack(side="left")

    # 保存先テキスト
    acvEnt = tk.Entry(acvFrm)
    acvEnt.configure(width=33)
    acvEnt.insert(0, "未選択")
    acvEnt.configure(state="disabled")
    acvEnt.pack(side="left")

    # 実行ボタン
    runBtn = tk.Button(wrpFrm)
    runBtn.configure(text="実行")
    runBtn.pack(
        anchor="e",
        pady=(0,5), padx=(0,5),
        ipadx=15, ipady=1)

    # 通知リスト
    msgList = tk.Listbox(wrpFrm)
    msgList.configure(height=6, width=65)
    msgList.pack()

    # 進捗バー
    pb = ttk.Progressbar(wrpFrm)
    pb.configure(
        maximum=10,
        orient="horizontal")
    pb.pack(pady=(4,0), fill="x")

    # 描画
    root.mainloop()


#-------------------------------------        
# メイン処理
#-------------------------------------
if __name__ == "__main__":
    print(DATE_STR)
    # 実行ホスト名確認関数
    #exeUserChk()
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

