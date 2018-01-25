# Headless Chrome

  Starting with Chrome 57, we can run Chrome as a **headless browser**. It is a way to run the Chrome browser in a headless       environment without the full browser UI.
  
  ## Pros
    
    * Tests script will be executed in the same environment as users of your site
    * Headless Chrome gives you a real browser context without the memory overhead of running a full version of Chrome.
    * Chrome is faster and more stable than PhantomJS. And it doesn’t eat memory like crazy
    
  ## Cons
  
    * If you need to do lots of debugging, headless debugging can be difficult.
    * You need to mimic real users
    
  ## Prerequisites
    
    * Google Chrome > 59
    * Chromedriver
    * Selenium
    * Python(You can also use java,ruby,javascrpit etc)
    
 ## Setup
     
   Now we will make a complete setup for headless chrome, for that we have to install all the prerequisties explained above.
   I have used _python_ for writing test script. Please click on this link [click here](https://duo.com/blog/driving-headless-chrome-with-python) for step by step instruction for installation of headless chrome.
  
  ## Example
  
  Below is the Python script for Facebook login using headless chrome .By executing this script user will first login facebbok after that it update his Facebook status.
  
  ```
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("headless")
```
 When we will open facebook's website then a alert message appears, we have to handle it.So i have used _chrome options_ to disable the notification. Below is code for the same.
 
 ```
 a = "path/of/your/chrome/driver"
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(str(a),   chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
driver.implicitly_wait (10)
driver.find_element_by_id("email").send_keys("Facebookid")
driver.find_element_by_id("pass").send_keys("password")
title1=driver.title
 ```
    
   
  
  
  
