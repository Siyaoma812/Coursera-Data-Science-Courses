#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:32:01 2018

@author: Sylvia
"""

# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def download_time(file_size, file_unit, bandwidth_size, bandwidth_unit):
    unit = [['kb', 2 ** 10],
            ['kB', 2 ** 10 * 8],
            ['Mb', 2 ** 20],
            ['MB', 2 ** 20 * 8],
            ['Gb', 2 ** 30],
            ['GB', 2 ** 30 * 8],
            ['Tb', 2 ** 40],
            ['TB', 2 ** 40 * 8]]
    i = 0
    while i < 8:
        if file_unit == unit[i][0]:
            file_size = file_size * unit[i][1]
        if bandwidth_unit == unit[i][0]:
            bandwidth_size = bandwidth_size * unit [i][1]
        i = i + 1
    hour = int(file_size / (bandwidth_size * 3600))
    minute = int((file_size - 3600*hour*bandwidth_size) / (bandwidth_size * 60))
    second = (file_size - hour * 3600 * bandwidth_size - minute * 60*bandwidth_size) / (bandwidth_size * 1.0)
    string = ""
    if hour == 1:
        string1 = "1 hour,"
    else:
        string1 = str(hour) + " hours,"
    if minute == 1:
        string2 = "1 minute,"
    else:
        string2 = str(minute) + " minutes,"
    if second == 1:
        string3 = "1 second"
    else:
        string3 = str(second) + " seconds"
    string = string1 + string2 + string3
    return string

            
    


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(3600)

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds