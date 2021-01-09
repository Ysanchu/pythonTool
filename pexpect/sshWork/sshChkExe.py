#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,datetime,pwd,subprocess
sys.path.append("./lib")
import pexpect


"""
■ 概要
  SSH接続確認ツール

■ 使用方法
   # python sshChkExe.py

   ※[./sshChk.list] の情報を元に、SSHコマンドを実行します。
   ※SSH接続がNGとなったものだけ標準出力します。
   ※実行結果のログは以下に格納されます。
     - ./result-NG.log : SSH接続NG結果
 　　- ./log/
        ├ prompt.log   : SSH実行ログ
        └ result.log   : SSH接続確認結果

■ 補足
  ・Support: python 2.6 - 2.7
  ・pexpectのライブラリ使用。
    [./lib/pexpect.py] が存在すること。
  ・パスワード要求が無い場合も対応済み。
  ・SSHコマンド実行中の結果は、別ターミナルから以下のコマンドで参照できます。
    # tail -F ./log/prompt.log

■改版履歴
   2020-07-16 1.0.0 yamanaka    新規作成
   2020-07-17 1.0.1 yamanaka    PasswordプロンプトのTimeout値を変更 1→3
                                その他誤記修正

"""
__author__  = "yamanaka yasuyuki"
__version__ = "1.0.1"
__date__    = "2020/07/17"



#-------------------------------------
# 定義部
#-------------------------------------
DEBUG_LOG_FILENAME = datetime.datetime.now().strftime('%Y%m%d%H%M%S_DEBUG.txt')
TIMEOUT         = 3            # SSH接続タイムアウト値
ROGIN_PROMPT    = '\$|#|>'        # ログインプロンプト文字列(正規表現)
PASSWORD_PROMPT = '[Pp]assword:'    # パスワード要求プロンプト文字列(正規表現)
SSHCONF_FILE    = './sshChk.list'    # SSHリストファイル
PROMPT_LOG      = './log/prompt.log'    # SSH実行ログ
RESULT_LOG      = './log/result.log'    # SSH接続確認結果
RESULT_NG_LOG   = './result-NG.log'    # SSH接続NG結果

#-----------------------------------
# 関数部
#-----------------------------------
# SSH接続実行
def sshChk():
    resultLogFile = open(RESULT_LOG , "w")    # SSH確認結果
    promptLog     = open(PROMPT_LOG , "wb")   # SSH実行ログ
    # SSHリストファイル読み込み
    fileName = SSHCONF_FILE
    # ファイルオープン
    with open(fileName,"r") as file:
        # 1行ずつ読み込み
        for line in file:
            # SSHリストファイルの文字列確認 (空白行、コメント行の無視対応)
            strChk = re.match(r"^#|^\n", line)
            if strChk:
                continue
                        # 先頭、末尾の空白文字列削除
            line = line.strip()
            # カンマ区切りでSSHリストファイル読み込み
            splitStr = line.split(',')
            try:
                hostName = splitStr[0].strip()    # ホスト名
                passStr  = splitStr[1].strip()    # パスワード文字列
                sshCom   = splitStr[2].strip()    # SSHコマンド文字列
            # SSHリストファイル読み込みエラー
            except:
                # ログファイル書き込み
                resultLogFile.write(line + " :    NG! 読み込みエラー。 [ " + SSHCONF_FILE + " ] を確認して下さい。\n")
                continue

            # ホスト名確認   (python2.6だとcheck_outputモジュールが無いエラー。。Popenで対処。)
            #hostChkComStr = subprocess.Popen("hostname" , stdout=subprocess.PIPE).communicate()[0].strip() # python2.6以前
            hostChkComStr = subprocess.check_output("hostname" , shell=True).strip()   # python2.7
            print(hostChkComStr)

            # ホスト名が一致しない場合はSSH実行しない
            if(hostName != hostChkComStr):
                continue

            # 標準出力
            print("  確認中 : " + sshCom)
            # ログファイル書き込み
            promptLog.write("★ : " + sshCom + "\n")
            # SSH接続確認実行
            try:
                sess = pexpect.spawn(sshCom , timeout=TIMEOUT)
                sess.logfile = promptLog   # 標準出力ログ
                # パスワード入力
                try:
                    sess.expect(PASSWORD_PROMPT , timeout=3)
                    sess.sendline(passStr)
                except:
                    # passwordが聞かれない場合は何もしない
                    pass
                sess.expect(ROGIN_PROMPT)
                sess.sendline("")        # Enterのみ押下
                sess.expect(ROGIN_PROMPT)
                # ログファイル書き込み
                resultLogFile.write(line + "  : OK!\n")
                promptLog.write("\n")
            # SSH接続失敗
            except:
                # ログファイル書き込み
                resultLogFile.write(line + " :    NG! 手動でSSH接続の確認をして下さい。\n")
                promptLog.write("\n")
                continue

# SSH接続結果確認
def resultChk():
    # NG結果標準出力 & ログ出力
    print("\n\n■NG結果")
    subprocess.call("grep NG! " + RESULT_LOG + " | tee " + RESULT_NG_LOG , shell=True)
    print("\n  ------------------------------------------------------------")
    print("  上記にSSH接続失敗<NG>の一覧を示しています。 [ " + RESULT_NG_LOG + " ]")
    print("  <NG>が存在した場合は、コマンドやパスワードを参照して手動で確認して下さい。")
    print("   ※プロンプトのログは [ "  + PROMPT_LOG + " ] に出力されています。")
    print("  ------------------------------------------------------------\n")

#-------------------------------------
# メイン処理
#-------------------------------------
if __name__ == "__main__":
    print("SSH接続確認実行中。しばらくお待ち下さい。")
    sshChk()    # SSH接続実行
    resultChk()    # SSH接続結果確認


