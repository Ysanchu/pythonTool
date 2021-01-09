
■ツール格納場所
  https://pjshr170.soln.jp/IJS90B0/ln/lib/O8Fkrpq
  12.STEP2.5  \10_コントローラ\90_商用化\phase5_NSO化開発\30_リリース提示物\ping-ssh接続確認Tool\
   ├pingChkTool.zip   : ping接続確認ツール
   └sshChkTool.zip    : ssh接続確認ツール

■ツール動作イメージ
  ===================================
 ・上記のツール「pingChkTool.zip」「sshChkTool.zip」を各サーバに
   配置して実行します。
 ・F更リハ、商用等で使用する場合は「pingChk.list」「sshChk.list」を更新して
   使用して下さい。
  ===================================

■ツール実行方法
  ------------------------------------------------------------
  1.ツール配置
    ツール実行するサーバに、「pingChkTool.zip」「sshChkTool.zip」を
    配置する。

  2.ツール展開
    # TOOLPUT_DIR="/tmp"
      ※ツールを配置したディレクトリに合わせる。

    # cd ${TOOLPUT_DIR}
    # ls -l pingChkTool.zip sshChkTool.zip
      ※ファイルが存在することを確認する。

    # unzip pingChkTool.zip
    # unzip sshChkTool.zip
      ※ツールが展開されることを確認する。


  3.ping接続ツール実行
    # cd pingChkTool
    # vim pingChk.list
      ※ping設定ファイルが正しいか確認する。
    # /bin/bash pingChkExe.sh
      ※ping接続がNGとなったものを標準出力します。
      ※詳しくは同ディレクトリの「README.txt」を参照。

  4.ssh接続ツール実行
    # cd ${TOOLPUT_DIR}/sshChkTool
    # vim sshChk.list
      ※ssh設定ファイルが正しいか確認する。
    # python sshChkExe.py
      ※SSH接続がNGとなったものを標準出力します。
      ※詳しくは同ディレクトリの「README.txt」を参照。
  ------------------------------------------------------------

■ツール削除方法
  ------------------------------------------------------------
  1.ツール削除
    # TOOLPUT_DIR="/tmp"
      ※ツールを配置したディレクトリに合わせる。
    # cd ${TOOLPUT_DIR}
    # ls -l pingChkTool.zip sshChkTool.zip
    # ls -ld pingChkTool sshChkTool
      ※ファイルが存在することを確認する。
    
    # rm -f pingChkTool.zip sshChkTool.zip
    # rm -rf pingChkTool sshChkTool

    # ls -l pingChkTool.zip sshChkTool.zip
    # ls -ld pingChkTool sshChkTool
      ※ファイルが削除されていることを確認
  ------------------------------------------------------------

