
■ 概要
   SSH接続確認ツール

■ 使用方法
   # vim ./sshChk.list
     ※SSH確認リストのファイルを更新する。

   # python sshChkExe.py
     ※SSH接続がNGとなったものを標準出力します。

■ディレクトリ構成
   ./sshChkExe.py    : SSH接続確認ツール
   ./sshChk.list     : SSH接続確認リスト
   ./result-NG.log   : SSH接続NG結果
   ./log/
     ├prompt.log     : SSH接続確認結果
     └result.log     : SSH実行ログ
   ./lib/
     └pexpect.py     : pexpectライブラリ

■ 出力例
  ==============================
   # python sshChkExe.py
   SSH接続確認実行中。しばらくお待ち下さい。
     確認中 : ssh maintenance@192.168.1.33 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null
     確認中 : ssh maintenance@192.168.1.34 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null

   ■NG結果
   sd-tstctl-och01 , #v3@dM0701    , ssh root@192.168.1.37 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null :    NG! 手動でSSH接続を確認して下さい。

     ------------------------------------------------------------
     上記にSSH接続失敗<NG>の一覧を示しています。 [ ./result-NG.log ]
     <NG>が存在した場合は、コマンドやパスワードを参照して手動で確認して下さい。
      ※プロンプトのログは [ ./log/prompt.log ] に出力されています。
     ------------------------------------------------------------

   #
   ==============================

■ 補足
  ・Support: python 2.6 - 2.7
  ・pexpectのライブラリ使用。
    [ ./lib/pexpect.py ] が存在すること。
  ・[ ./sshChk.list ] の情報を元に、SSHコマンドを実行する。
  ・パスワード要求が無い場合も対応済み。
  ・SSHコマンド実行中の結果は、別ターミナルから以下のコマンドで参照できます。
    # tail -F ./log/prompt.log

■改版履歴
  2020-07-16 1.0.0 yamanaka    新規作成
  2020-07-17 1.0.1 yamanaka    PasswordプロンプトのTimeout値を変更 1→3
                               その他誤記修正

