#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 06:58:59 2018

@author: Sylvia
"""

#Following Links in Python

#In this assignment you will write a Python program that expands on 
#http://www.py4e.com/code3/urllinks.py. The program will use urllib to 
#read the HTML from the data files below, extract the href= vaues from 
#the anchor tags, scan for a tag that is in a particular position relative 
#to the first name in the list, follow that link and repeat the process a 
#number of times and report the last name you find.

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL-')
repeat = input('Repeat Times-')
position = input('Target Position-')

count = 0

while count<int(repeat):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    pos = 0
    for line in tags: 
        pos+=1
        if pos == int(position):
            print (line.contents[0])
            url = line.get('href')
    count+=1



    
        
        

