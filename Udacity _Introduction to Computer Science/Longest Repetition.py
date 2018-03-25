#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:39:55 2018

@author: Sylvia
"""

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(list):
    if list == []:
        return None
    else:
        previous = 0
        current = 1
        i = 1
        number = list[0]
        output = number
        while i < len(list):
            if number == list[i]:
                current = current + 1
            else:
                if previous < current:
                    previous = current
                    output = number
                    number = list[i]
                    current = 1
                else:
                    current = 1
                    number = list[i]
            i = i + 1
        if previous < current:
            output = number
    return output


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2,2,3,3,4,4,4])

