# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:48:35 2023

@author: User
"""
#IMPORT THE REQUIRED LIBRARIES
from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.by import By

#LINK TO LOAD THE PAGE
url='https://www.amazon.in/s?k=laptops&page='+str(int(1))

#LOADING THE WEBDRIVER
driver=webdriver.Edge('C:/Users/User/Documents/EdgeWebdriver/msedgedriver.exe')
driver.get('https://www.amazon.in')
sleep(2)

#FINDING THE SEARCH BOX AND SUBMIT BOX
input_search=driver.find_element_by_id("twotabsearchtextbox")
search_button=driver.find_element_by_xpath('.//input[@type="submit"]')

#ENTERING THE ELEMENT TO SEARCH
input_search.send_keys("Laptops")
sleep(2)
search_button.click()

#RANGE BASED ON THE NUMBER OF PAGES TO SCRAPE
Products=[]
for i in range(10):
    print("Scrapped pages:",i+1)
    product=driver.find_elements_by_xpath('.//div[@class="a-section a-spacing-small a-spacing-top-small"]')
    for p in product:
        Products.append(p.text)
        sleep(2)
    next_page=driver.find_element_by_xpath('.//span[@class="s-pagination-item s-pagination-disabled"]')
    next_page.click()
  
#LENGTH OF PRODUCTS
len(Products)

Products[5]

Products
