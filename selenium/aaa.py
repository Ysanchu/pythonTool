#!/usr/local/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
time.sleep(5)	# timeライブラリが無いとエラーが発生するので注意

driver.close()
