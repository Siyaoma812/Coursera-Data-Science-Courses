#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 06:39:28 2018

@author: Sylvia
"""
#In this assignment you will write a Python program somewhat similar 
#to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, 
#read the XML data from that URL using urllib and then parse and extract the 
#comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you 
#the sum for your testing and the other is the actual data you need to process for 
#the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_63410.xml (Sum ends with 30)
#You do not need to save these files to your folder since your program will read the data 
#directly from the URL. Note: Each student will have a distinct data url for the 
#assignment - so only use your own data url for analysis.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL-')
print ('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')

count = 0
sum = 0
for item in lst:
    count +=1
    sum += int(item.find('count').text)

print ('count', count)
print ('sum', sum)
    
    
