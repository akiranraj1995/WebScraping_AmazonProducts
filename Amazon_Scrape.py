# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:48:35 2023

@author: User
"""

from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.by import By

#url='https://www.amazon.in/s?k=laptops&page='+str(int(1))
driver=webdriver.Edge('C:/Users/User/Documents/EdgeWebdriver/msedgedriver.exe')
driver.get('https://www.amazon.in')
sleep(2)

'''
input_search=driver.find_element_by_xpath('.//input[@id="twotabsearchtextbox"]')
search_button=driver.find_element_by_xpath('.//input[@id="nav-search-submit-button"]')
'''
input_search=driver.find_element_by_id("twotabsearchtextbox")
search_button=driver.find_element_by_xpath('.//input[@type="submit"]')

input_search.send_keys("Laptops")
sleep(2)
search_button.click()

Products=[]
for i in range(10):
    print("Scrapped pages:",i+1)
    product=driver.find_elements_by_xpath('.//div[@class="a-section a-spacing-small a-spacing-top-small"]')
    for p in product:
        Products.append(p.text)
        sleep(2)
    next_page=driver.find_element_by_xpath('.//span[@class="s-pagination-item s-pagination-disabled"]')
    next_page.click()
    
len(Products)

Products[5]

Products
''' 
driver.find_elements_by_xpath('.//div[@class="sg-col-inner"]')
el=driver.find_elements_by_xpath('.//div[@class="a-section"]')
sleep(4)


driver.find_elements_by_xpath('.//div[@class="sg-col-inner"]')
el=driver.find_elements_by_tag_name('h2')
for ele in el:
    print(len(ele))

links=driver.find_elements(By.TAG_NAME,"a")
len(links)

for link in links:
    print(link.text)
    
'''
