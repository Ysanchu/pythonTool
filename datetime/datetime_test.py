#!/usr/local/bin/python3
import datetime

"""
  参考) Python日付型
  https://qiita.com/motoki1990/items/8275dbe02d5fd5fa6d2d
"""

def dateChk():
    print(datetime.date.today())
    print(datetime.datetime.today())
    print(datetime.date(2017, 11, 12))
    print(datetime.datetime(2017, 11, 12, 9, 55, 28))
    
    #0:月曜日,1:火曜日,2:水曜日,3:木曜日,4:金曜日,5:土曜日,6:日曜日
    print(datetime.date(2017, 11, 11).weekday())

    # time.struct_time(tm_year=2017,tm_mon=11,tm_mday=12,tm_hour=9,
    # tm_min=55, tm_sec=28, tm_wday=6, tm_yday=316, tm_isdst=0)
    now = datetime.datetime(2017, 11, 12, 9, 55, 28)
    print(now.timetuple()) 

    #todayStr = "{0:%Y/%m/%d}".format(datetime.date.today())
    todayStr = "{0:%Y%m%d-%H%M%S}".format(datetime.datetime.today())
    print(todayStr)

    todayStr2 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    print(todayStr2)

# Main
if __name__ == "__main__":
    dateChk()

