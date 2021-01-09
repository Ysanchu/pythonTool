#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess
import pexpect
import pdb
#import termcolor

"""
python作成の定型文
Usage :
"""

__author__  = 'SANCHU'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

PASSWORD_PROMPTS=["パスワード:", "password:"]
ROGIN_PRONPT = "\$|#"         # ログインプロンプト文字列
TIMEOUT      = 3              # タイムアウト値設定
DEBUG_LOG  = None
SSHCONF_FILE = 'ssh.list'     # SSH設定ファイル
PROMPT_LOG   = 'prompt.log'   # SSH実行ログ
RESULT_LOG   = 'result.log'   # SSH接続確認ログ
 

def fileRead():
    # 結果ファイル
    resultLogFile = open(RESULT_LOG , "w")   # SSH確認結果
    promptLog     = open(PROMPT_LOG , "wb")  # SSH実行ログ
    # SSHリストファイル読み込み
    fileName = SSHCONF_FILE 
    # ファイルオープン
    with open(fileName,"r") as file:
        # 1行ずつ読み込み
        for line in file:
            # リストファイル文字列確認 (空白行、コメントの無視対応)
            strChk = re.match(r"#|^\n", line)
            if strChk:
                continue
            # 文字列の空白、改行削除 (先頭・末尾)
            line = line.strip()
            # カンマ区切り
            splitStr = line.split(',')
            try:
                hostName = splitStr[0].strip()   # ホスト名
                passStr  = splitStr[1].strip()   # パスワード文字列
                sshCom   = splitStr[2].strip()   # sshコマンド文字列
            except:
                print(line + " : 読み込みエラー")
                continue
            # ログファイル書き込み
            resultLogFile.write(sshCom)
            promptLog.write("★ : " + sshCom + "\n")
            # ssh接続確認実行
            try:
                sess = pexpect.spawn(sshCom , timeout=TIMEOUT)
                sess.logfile = promptLog    # 標準出力★ 
                # パスワード入力
                try:
                    sess.expect('[Pp]assword:' , timeout=3)
                    sess.sendline(passStr)
                except:
                    #print("")
                    pass
                sess.expect(ROGIN_PRONPT)
                sess.sendline("uname -n")
                sess.expect(ROGIN_PRONPT)
                sess.sendline("echo $?")
                sess.expect(ROGIN_PRONPT)
                #subprocess.call("echo $?" , shell=True)
                resultLogFile.write(" : OK!\n")
                promptLog.write("\n")
            # ssh接続失敗
            except:
                # ログファイル書き込み
                resultLogFile.write(" :    NG!\n")
                promptLog.write("\n")
                continue


def resultChk():
    subprocess.call("grep NG! " + RESULT_LOG + " | tee result-NG.log", shell=True)
    print("\n  上記でSSH接続に失敗しています")
    print("  コマンドやパスワードを確認して、手動で確認して下さい。")
    print("  ※プロンプトのログは" + PROMPT_LOG + "に出力されています。\n")

# Main
if __name__ == "__main__":
    fileRead()
    resultChk()



