'''
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS() # or webdriver.Firefox()
a = [лист русских букв]
for i in a:

    driver.get('здесь url страницы + переменная буква')

    html = driver.page_source.encode('utf-8')
    b = BeautifulSoup(html, 'lxml')
    items = b.find_all('тег', attrs={'id':'айди тега'})
    print(len(items))
'''
