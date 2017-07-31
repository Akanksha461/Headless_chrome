import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'`
a= "/home/akanksha/Downloads/going_headless/chromedriver"
driver = webdriver.Chrome(str(a),   chrome_options=chrome_options)
#driver = webdriver.Chrome(str(a),   chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
title1=driver.title
print(title1)