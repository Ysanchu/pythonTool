#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
sleep(10)
driver.get("https://liginc.co.jp/")

sleep(10)

driver.find_element_by_class_name('header-search-button')
driver.find_element_by_class_name('header-search-input').send_keys('ともぞう', Keys.ENTER)

# 5秒待機する
sleep(5)

# ブラウザの終了
driver.close()
