import re

sum = 0

hand = open('actual data.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('[0-9]+', line)
	if not x:
		continue
	else:
		for i in x:
			sum += int(i)
print(sum)
