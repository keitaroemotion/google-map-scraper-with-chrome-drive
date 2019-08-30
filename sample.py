#!/usr/bin/env python

from datetime                      import datetime
from selenium                      import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as ec

import logging
import re
import time

logging.basicConfig(filename="chrome.log", level=logging.DEBUG)

def sleep(x):
    if(x == 0):
        return
    print("waiting ... {} ".format(x))
    time.sleep(1)
    sleep(x - 1)

def get_element(driver, wait, key, value):
    tag = '//*[@{}="{}"]'.format(key, value)
    wait.until(ec.visibility_of_element_located((By.XPATH, tag)))
    return driver.find_element_by_xpath(tag)

def write_log(text):
    print(text)
    logging.info("{}|{}".format(datetime.now, text))

def get_option():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return options

def query_google_map(key):
    driver = webdriver.Chrome(options=get_option())
    wait = WebDriverWait(driver, 7)
  # driver.get("https://www.google.com/search?q=italian&tbm=lcl")
  # driver.get("https://www.google.com/search?adtest=on&q=italian&tbm=lcl")
    driver.get("https://www.google.com/search?adtest=on&query=%E6%9C%AD%E5%B9%8C+%E3%82%82%E3%81%A4%E9%8D%8B&uule=w+CAIQICIWc2FwcG9ybyxob2trYWlkbyxqYXBhbg&pws=0&hl=ja&tbm=lcl&glp=1&tci=g:1009076")

    write_log(get_element(driver, wait, "class", "BBj6N"))
    write_log(get_element(driver, wait, "id",    "rcnt"))
    write_log(get_element(driver, wait, "id",    "search"))
    write_log(get_element(driver, wait, "class", "rl_full-list"))
    write_log(get_element(driver, wait, "id",    "rl_ist0"))
    write_log("accessed!")
    driver.close()
    driver.quit()
    sleep(1)
    query_google_map(key)

key="italian"
query_google_map(key)
