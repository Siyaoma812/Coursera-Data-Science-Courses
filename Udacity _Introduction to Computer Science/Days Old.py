#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:20:00 2018

@author: Sylvia
"""
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenYear(year1,year2):
    n=(year2-year1)/4
    r=(year2-year1)%4
    if year1==year2:
        return 0
    else:
        if leapYear(year1):
            return n * (366 + 365 * 3) + 366 + 365 * (r - 1)
        else:
            if year1 % 100 == 0:
                if r == 0:
                    return 4 * 365 + (n - 1) * (366 + 3 * 365)
                else:
                    return 4 * 365 + (n - 1) * (366 + 3 * 365) + 366 + 365 * (r - 1)
            else:
                if r == 0:
                    return n * (365 * 3 + 366)
                else:
                    if r == year1 % 4:
                        return n * (366 + 365 * 3) + 365 * (r - 1) + 366
                    else:
                        return n * (366 + 365 * 3) + 365 * r

def leapYear(year):
    if year%4!=0:
        return False
    else:
        if year%100==0:
            return year%400==0
        else:
            return True


def daysInMonth(year1,month1):
    if month1==1 or month1==3 or month1==5 or month1==7 or month1==8 or month1==10 or month1==12:
        return 31
    else:
        if month1==2:
            if leapYear(year1):
                return 29
            else:
                return 28
        else:
            if month1==0:
                return 0
            else:
                return 30

def daysBetweenMonth (year1,month1):
    i=month1-1
    k=0
    while 0<=i:
        k=k+daysInMonth(year1,i)
        i=(i-1)
    return k
def days(day1,day2):
    return day2-day1

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    y=daysBetweenYear(year1,year2)
    m=daysBetweenMonth(year2,month2)-daysBetweenMonth(year1,month1)
    d=days(day1,day2)

    return y+m+d

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

