from selenium import webdriver

path = 'D:\drive\Colab Notebooks\webScrape\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)
urlLink = 'https://www.python.org/'

driver.get(url=urlLink)
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}
for i in range(len(event_times)):
    events[i] = {
        'time' : event_times[i].text,
        'name' : event_names[i].text
    }

print(events)
driver.close()
driver.quit()
