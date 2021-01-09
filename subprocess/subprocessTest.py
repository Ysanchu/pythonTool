#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess

"""
python作成の定型文
Usage :
"""

__author__  = 'SANCHU'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

def testFunc():
    cmd = "ls -l"
    subprocess.call(cmd.split())
    print("------------------------------")
    subprocess.call(["ls","-la"])
    # 結果を変数に格納
    res = subprocess.check_output("cal", shell=True)
    print(res)
    print("------------------------------")
    print(res.decode(encoding='utf-8')) # Encode🌟

    # パイプライン できる/できない
    #subprocess.call('find . -type f | grep txt$'.split())              # できない。。
    #subprocess.run("find . -type f | grep txt$" , shell=True, text=True) #できる❗



def testFunc2():
    TAR_LIST = "tar.list"
    subprocess.call("ls -l".split())
    print("------------------------------")
    subprocess.run("find . -type f | grep txt$ > " + TAR_LIST  , shell=True, text=True)
    subprocess.run("ls -l " + TAR_LIST , shell=True, text=True)




# Main
if __name__ == "__main__":
    testFunc()

