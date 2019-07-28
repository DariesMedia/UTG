# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:17:14 2019

@author: PASTOR DAN

UNDETECTABLE ULTIMATE TRAFFIC GENERATOR THAT EXHIBIS HUMAN BEHAVIOUR
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from random import choice as cc
from time import sleep


Window_size = ["window-size=1400, 1050", "window-size=800, 600", "window-size=1024, 768", "window-size=1280, 800", "window-size=1440, 900", "window-size=1280, 1024", "window-size=1400, 1050", "window-size=1680, 1050", "window-size=1600, 1200", "window-size=1920, 1200"]

proxy= ['--proxy-server=12.133.183.51:8080', '--proxy-server=40.117.231.19:3128', '--proxy-server=138.197.108.5:3128', '--proxy-server=69.132.115.163:50909', '--proxy-server=148.66.38.193:33899', '--proxy-server=103.209.176.133:57839', '--proxy-server=103.212.92.225:42063', '--proxy-server=191.54.234.141:3128', '--proxy-server=168.90.50.118:39037', '--proxy-server=45.231.213.110:54416', '--proxy-server=142.93.144.177:808', '--proxy-server=35.176.53.80:3128']

tyme = [5, 6, 7, 8] 

post_time = [10, 20, 30, 40]

post = []

per_visit = [1,2]

LINK = [""]

def UTG():
    h = cc(proxy)
    
    for i in proxy:
        if i == h:
            proxy.remove(h)
            
    # Using Selenium
    options = Options()
    options.add_argument(cc(Window_size))
    ua = UserAgent().random
    user_agent = ua    # ua.random
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument(h)
    chrome = webdriver.Chrome(r"C:\Users\PASTOR DAN\Documents\DAN THE GURU\PYTHONPROJECTS\chromedriver", chrome_options=options)
    
    # chrome.get('https://whoer.net/')
    try:
        try:
            chrome.get(LINK)
            chrome.get(LINK)
        except:
            chrome.get(LINK)
        sleep(cc(tyme))
        
        post_url= chrome.find_elements_by_class_name("retitle")
        for i in post_url:
        # k = chrome.find_element_by_link_text(i.text)
        # k = k.get_attribute("href")
            post.append(i.text)
        
        visit = cc(per_visit) 
          
        for i in range(visit):
            chrome.find_element_by_link_text(cc(post)).click()
            sleep(cc(tyme)) 
            chrome.execute_script("window.scrollBy(0,600);")
            sleep(cc(post_time))
            chrome.execute_script("window.scrollBy(0,500);")
            sleep(cc(post_time))
            chrome.execute_script("window.scrollBy(0,700);")
            sleep(cc(post_time))
            chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            chrome.execute_script("window.history.go(-1)")
            sleep(cc(tyme))  
        
        
         
        chrome.find_element_by_id('page-5345').click()
        sleep(5)
        chrome.execute_script("window.scrollBy(0,600);")
        
        chrome.quit()
    except:
        chrome.quit()
        print(UTG())
        
        

time_per_lunch = [3, 4, 5, 7, 8, 10, 12]
count = 0
for i in range(100):
    count = +1
    print(UTG())
    sleep(cc(time_per_lunch))    
    




        



