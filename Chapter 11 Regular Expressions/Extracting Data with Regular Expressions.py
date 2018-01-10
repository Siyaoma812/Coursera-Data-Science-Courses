#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

import re

sum = 0

hand = open('regex_sum_63406.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('[0-9]+', line)
	if not x:
		continue
	else:
		for i in x:
			sum += int(i)
print(sum)
