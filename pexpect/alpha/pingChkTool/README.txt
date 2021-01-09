
■ 概要
   ping接続確認ツール

■ 使用方法
   # vim ./sshChk.list
     ※ping確認リストのファイルを更新する。

   # /bin/bash pingChkExe.sh
     ※ping接続がNGとなったものを標準出力します。

■　ディレクトリ構成
   ./pingChkExe.sh      : ping接続確認ツール
   ./pingChk.list       : ping接続確認リスト
   ./result-NG.log      : ping接続NG結果
   ./log/
     └ pingResult.log   : ping接続確認結果

■ 出力例
   ==============================
   # /bin/bash pingChkExe.sh
   ping接続確認実行中。しばらくお待ち下さい。


   ■NG結果
   sd-tstctl-och01   ,  ping -I 10.20.10.7 -c 1 10.10.10.10 :    NG!

     ------------------------------------------------------------
     上記にping接続失敗<NG>の一覧を示しています。 [ ./result-NG.log ]
     <NG>が存在した場合は、コマンドを参照して手動で確認して下さい。
      ※ 実施したpingコマンドは [ ./log/pingResult.log] で確認できます。
     ------------------------------------------------------------

   #
   ==============================

■ 補足

■ 改版履歴
   2020-07-16  1.0.0 新規作成  yamanaka


