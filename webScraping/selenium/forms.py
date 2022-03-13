from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = 'D:\drive\Colab Notebooks\webScrape\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)
url = 'http://secure-retreat-92358.herokuapp.com/'

driver.get(url=url)


fname = driver.find_element_by_name('fName')
fname.send_keys("vishwanath")
lname = driver.find_element_by_name('lName')
lname.send_keys("reddy")
email = driver.find_element_by_name('email')
email.send_keys("vishwanathreddyaenugu@gmail.com")

signup_button = driver.find_element_by_css_selector("form button")
signup_button.click()

time.sleep(10)
driver.close()
driver.quit()
