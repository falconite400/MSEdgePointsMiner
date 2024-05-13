import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import sys

# setup
def wait_for(sec=2):
    time.sleep(sec)

search_list = [x for x in range(34)]

driver = webdriver.Edge(service=Service('C:\\Users\\%username%\\code\\msepointsminer\\msedgedriver.exe'))
url_base = 'http://www.bing.com/search?q='
wait_for(5)

# edge auto-logs in, delay so it can sign in
driver.get('https://bing.com')
wait_for(10)

for s in search_list:    
    try:
        driver.get(url_base + str(s))
    except Exception as e:
        print(e)
    wait_for()

# clean up
driver.close()
sys.exit()