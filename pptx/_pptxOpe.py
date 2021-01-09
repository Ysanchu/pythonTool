#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,csv,pwd,subprocess
sys.path.append('./src/Pillow-7.1.2')
sys.path.append('./src/Pillow-7.1.2/Tests/')
sys.path.append('./src/Pillow-7.1.2/src')
sys.path.append('./src/XlsxWriter-1.2.9')
sys.path.append('./src/lxml-4.5.1')
sys.path.append('./src/python-pptx-0.6.18')
from PIL import Image
from pptx import Presentation


"""
python作成の定型文
Usage :
"""

# 環境定義
#---------------------------
__author__  = 'SANCHU'
__version__ = '1.0.0'
__date__    = 'YYYY/MM/DD'

# テスト関数
#---------------------------
def testFunc():
    print("testFunc")

# Main
#===========================
if __name__ == "__main__":
    testFunc()

