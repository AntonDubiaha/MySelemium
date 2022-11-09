from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
#for cookie save
import pickle


option = webdriver.FirefoxOptions()
#open without frontend
option.headless = True
browser = webdriver.Firefox(options=option)

browser = webdriver.Firefox()
browser.get('https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE')
#timer on 5sec
time.sleep(5)
#take screenshot
browser.save_screenshot('screen1')
browser.refresh
browser.quit

#article
css_selector = '.sku > span:nth-child(1)'
article = browser.find_element(By.CSS_SELECTOR, css_selector)
CSS_SELECTOR = '#sku-148136'
article_value = browser.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
result = (f'{str(article.text)} {str(article_value.text)} \n')

#наявність для поставки
css_selector = '.additional-details > div:nth-child(2) > a:nth-child(1)'
name = browser.find_element(By.CSS_SELECTOR, css_selector)
CSS_SELECTOR = '.additional-details > div:nth-child(2) > span:nth-child(2)'
value = browser.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
result += (f'{str(name.text)} {str(value.text)} \n')

#прогноз наявності в Польщі
css_selector = '.additional-details > div:nth-child(3) > a:nth-child(1)'
name1 = browser.find_element(By.CSS_SELECTOR, css_selector)
CSS_SELECTOR = '.additional-details > div:nth-child(3) > span:nth-child(2)'
value1 = browser.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
result += (f'{str(name1.text)} {str(value1.text)} \n')

#Наявність у Львові
css_selector = '.additional-details > div:nth-child(5) > a:nth-child(1)'
name2 = browser.find_element(By.CSS_SELECTOR, css_selector)
CSS_SELECTOR = '.additional-details > div:nth-child(5) > span:nth-child(2)'
value2 = browser.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
result += (f'{str(name2.text)} {str(value2.text)} \n')

#find all elements
browser.find_elements

#writing to file
with open('test.txt', 'w') as txt:
    txt.write(result)
    
#find attribute
example = browser.find_element(By.XPATH, 'xpath')
attribute = example.get_attribute('class')

#click on element
browser.find_element(By.XPATH, 'xpath').click()

#enter text
browser.find_element(By.XPATH, 'xpath').send_keys('Example text')

#scroling page and use keyboard keys
html = browser.find_element(By.TAG_NAME, ('html'))
for i in range(10):
    html.send_keys(Keys.DOWN)


#save cookie, 'wb' its record in bytes
#first open browser and link
pickle.dump(browser.get_cookies(), open('file.example', 'wb'))

#load cookies
#first open browser and link
for cookie in pickle.load(open('example.file', 'rd')):
    browser.add_cookie
#link refresh