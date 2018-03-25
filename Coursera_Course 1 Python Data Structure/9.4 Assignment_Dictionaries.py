#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest
# number of mail messages. The program looks for 'From ' lines and takes the second word of those lines
# as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
words = list()
for line in handle:
    if line.startswith('From:'):
        word = line.split()
        words.append(word[1])
for sender in words:
    counts[sender] = counts.get(sender, 0) + 1

print(counts)
max1 = 0
maxi = None
for key in counts:
    if counts[key] > max1:
        maxi = key
        max1 = counts[key]
print(maxi, max1)