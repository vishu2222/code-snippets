from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = 'D:\drive\Colab Notebooks\webScrape\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)
url = 'https://www.linkedin.com/login'

driver.get(url=url)
username = '.....@gmail.com'
pwd = ''

un = driver.find_element_by_id("username")
un.send_keys(username)
pd = driver.find_element_by_id('password')
pd.send_keys(pwd)
signin = driver.find_element_by_class_name('login__form_action_container')
signin.click()




time.sleep(30*60)
driver.close()
driver.quit()
