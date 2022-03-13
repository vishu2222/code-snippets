from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = 'D:\drive\Colab Notebooks\webScrape\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)
url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(url=url)

cookie = driver.find_element_by_id("cookie")
state = True
while state:
    cookie.click()

time.sleep(10)
driver.close()
driver.quit()