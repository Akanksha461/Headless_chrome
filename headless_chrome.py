import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("headless")

a = "/home/aj/going_headless/chromedriver"
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(str(a),   chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
driver.implicitly_wait (10)
driver.find_element_by_id("email").send_keys("id")
driver.find_element_by_id("pass").send_keys("password")
title1=driver.title
print(title1)
driver.find_element_by_id("loginbutton").click()
time.sleep(4)
driver.find_element_by_name("xhpc_message").send_keys("D")
# driver.find_element_by_css_selector('[placeholder="Share an update, Akanksha."]').send_keys("hello")
driver.find_element_by_xpath('(//*[@class="_2ph- _4-u3"])[2]').click()
print('pagal')
