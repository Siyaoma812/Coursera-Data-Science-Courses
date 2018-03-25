#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:38:39 2018

@author: Sylvia
"""

# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

def triangular(n):
    output = 0
    for element in range(1, n+1):
        output = output + element
    return output 
        
        
        



print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55
