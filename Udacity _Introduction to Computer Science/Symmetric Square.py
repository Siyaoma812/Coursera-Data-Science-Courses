#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:25:54 2018

@author: Sylvia
"""

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(arr):
    # Your code here
    i=0
    while i < len(arr):
        l = len(arr[i])
        if len(arr) != l:
            return False
        j = i
        while j < len(arr):
            if arr[i][j] == arr[j][i]:
                j = j + 1
            else:
                return False
        i = i + 1
    return True

print symmetric([[1, 2, 3],
               [2, 3, 4],
             [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
["dog", "dog", "fish"],["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
             ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
            [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
            [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
               [2,3,1]])
#>>> False