#!/usr/local/bin/python3
import pandas_datareader.data as pdr
import datetime

end   = datetime.date.today()
start = end - datetime.timedelta(days=5)

#print(start + ' : ' + end)
print("start {} : end {}".format(start, end))

# 以下のDocs参考すること
# https://pandas-datareader.readthedocs.io/en/latest/index.html

# 以下エラー。。
###pd_data = pdr.DataReader('SNE', 'iex', start, end)
###pd_data = pdr.DataReader('NASDAQ', 'iex', start, end)
###print(pd_data)
###f = pdr.DataReader('SNE', 'morningstar', start, end)

df = pdr.get_data_fred('GS10')
print(df)



