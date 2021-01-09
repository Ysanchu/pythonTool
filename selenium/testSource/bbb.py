#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("./chromedriver")
driver.get("http://swks.sakura.ne.jp/wars/kifusearch/")

try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_gtype_2")))
except Exception:
    driver.quit()

driver.execute_script("arguments[0].click();", elem)


