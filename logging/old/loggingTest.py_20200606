#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess
import logging
"""
python作成の定型文
Usage :

■Python_logging
 https://docs.python.org/ja/3/howto/logging.html
"""

__author__  = 'SANCHU'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

# テスト関数
#---------------------------
def testFunc():
    print("testFunc")
    #logging.basicConfig(format='%(asctime)s %(message)s' , datefmt='%Y/%d/%m %I:%M:%S')
    logging.basicConfig(filename='example.log',level=logging.DEBUG,    \
        format='%(asctime)s   <%(levelname)s> %(name)s - %(message)s', \
        datefmt='%Y-%d-%m %I:%M:%S')
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

# Main
#===========================
if __name__ == "__main__":
    testFunc()

