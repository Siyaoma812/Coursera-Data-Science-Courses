#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:46:02 2018

@author: Sylvia
"""
#Scraping Numbers from HTML using BeautifulSoup In this assignment 
#you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
#The program will use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers and compute the sum of the numbers in the file.

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input ('Enter - ')
html = urlopen(url, context = ctx).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
print
sum = 0
count = 0
for span in tags:
   sum +=int(span.string)
print (sum)
    
