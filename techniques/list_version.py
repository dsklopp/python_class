#!/usr/bin/python

f=open('afile.txt')
lines=[" ".join(line.strip().split()[1:]) for line in f ]
count=0
for line in lines:
	count+=1
print(str(count) + " lines present")
raw_input()
