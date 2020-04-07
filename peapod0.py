#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

url = browser.command_executor._url
session_id = browser.session_id
print('session url')
print(url)
print('session id')
print(session_id)
