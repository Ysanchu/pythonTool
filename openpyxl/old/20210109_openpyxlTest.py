#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess
sys.path.append('./src/et_xmlfile-1.0.1')
sys.path.append('./src/jdcal-1.4.1')
sys.path.append('./src/openpyxl-3.0.3/')
import openpyxl


"""
python作成の定型文
Usage :
"""

# 環境定義
#---------------------------
__author__  = 'SANCHU'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

WB = openpyxl.load_workbook('20200614_pythonTest.xlsx')

# テスト関数
#---------------------------
def testFunc():
    print("testFunc")
    print(type(WB))
    print(WB.sheetnames)
    sheet = WB['Sheet1']
    print(type(sheet))
    cell = sheet['A2']
    print(type(cell))
    print(cell.value)
    cell = sheet.cell(row=2, column=2)
    print(cell.value)

def testFunc2():
    print("testFunc2")
    sheet = WB['Sheet1']
    for rows in sheet.iter_rows(min_row=1, min_col=1, max_row=20, max_col=20):
        print()
        for cell in rows:
            print(cell.value , end=',')

# Main
#===========================
if __name__ == "__main__":
    #testFunc()
    testFunc2()

