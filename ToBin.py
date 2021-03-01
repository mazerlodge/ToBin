#!/bin/python3 

"""
	Convert the phrase specified by filename (in fn) to ascii values, output as binary. 
	
"""

fn = "dare.txt" 

file = open(fn, "r") 
lines = file.readlines() 
file.close() 

phrase = lines[0]

print("a vals = ", end='') 
for achar in phrase.upper():
	aVal = ord(achar)
	print(aVal, end=' ') 
print() 

print("r vals = ", end='') 
for achar in phrase.upper():
	aVal = ord(achar)
	if (aVal-64 > 0):
		print("%02d" % (aVal-64), end=' ') 
	else:
		print ("  ", end=' ')
print() 

for x in range(8,0,-1):
	print(x, end=' ') 
print() 
print('----------------')

for achar in phrase.upper():
	workingV = ord(achar)
	for x in range(7,-1,-1):
		currP = 2**x
		if (workingV >= currP):
			workingV = workingV - currP 
			msg = '1'
		else:
			msg = '0'

		print(msg, end=' ')
		
	print(" %s" % achar) 


