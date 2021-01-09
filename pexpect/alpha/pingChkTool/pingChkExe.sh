#!/bin/bash
#######################################
## ■ 概要
##   ping接続確認ツール
##
## ■ 使用方法
##    # /bin/bash pingChkExe.sh
##
##    ※[./sshChk.list] の情報を元に、pingコマンドを実行します。
##
## ■ 補足
##
## ■ 改版履歴
##    2020-07-16  1.0.0 新規作成  yamanaka
########################################
#-------------------------------------
# 定義部
#-------------------------------------
RETURN_OK=0
RETURN_NG=1

PINGCONF_FILE="pingChk.list"		# ping設定ファイル
RESULT_LOG="./log/pingResult.log"	# ping結果ログ
RESULT_NG_LOG="./result-NG.log"		# ping結果NGログ

#-----------------------------------
# 関数部
#-----------------------------------
# ping接続確認関数
pingChkExe()
{
	# ping設定ファイル読み込み
	cat ${PINGCONF_FILE} | while read line
	do
		# リストファイル文字列確認 (空白行、コメント文は無視)
		if [[ ${line} =~ ^#|^$ ]];then
			continue
		fi

		# リストファイル確認
		# ホスト名取得     (先頭行と末尾の空白文字列を削除)
		hostStr=`echo ${line} | cut -d ',' -f 1 | sed "s/^ +| +$//g"`
		# pingコマンド取得 (先頭行と末尾の空白文字列を削除)
		pingCom=`echo ${line} | cut -d ',' -f 2 | sed "s/^ +| +$//g"`
		# ホスト名確認
		hostComChk=`hostname`

		# ホスト名が異なる時は実施しない
		if [ ${hostStr} != ${hostComChk} ];then
			continue
		fi

		# pingコマンド確認 (※時間短縮のため、[-w 1]オプション追加)
		${pingCom} -w 1 > /dev/null 2>&1
		# ping疎通OK
		if [ $? -eq 0 ];then
    			echo "${line} : OK" >> ${RESULT_LOG}
		# ping疎通NG
		else
    			echo "${line} :    NG!" >> ${RESULT_LOG}
		fi
	done
}

#-------------------------------------
# メイン処理
#-------------------------------------
# ping結果ログファイル初期化
rm -f ${RESULT_LOG}

echo "ping接続確認実行中。しばらくお待ち下さい。"

# ping接続確認実行
pingChkExe

# ping疎通NGを標準出力 & ログ出力
echo -e "\n\n■NG結果"
cat ${RESULT_LOG} | grep "NG!" | tee ${RESULT_NG_LOG}
cat <<-EOF

  ------------------------------------------------------------
  上記にping接続失敗<NG>の一覧を示しています。 [ ${RESULT_NG_LOG} ]
  <NG>が存在した場合は、コマンドを参照して手動で確認して下さい。
   ※ 実施したpingコマンドは [ ${RESULT_LOG}] で確認できます。
  ------------------------------------------------------------

EOF

exit ${RETURN_OK}

