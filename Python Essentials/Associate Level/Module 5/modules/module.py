#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#print("I like to be a module")

#print(__name__)
###################################

#counter = 0

#if __name__ ==  "__main__":
#    print("I prefer to be a module")
#else:
#    print("I like to be a module")

############################################
# module.py

#!/usr/bin/env python3 

""" module.py - an example of Python module """

__counter = 0

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ ==  "__main__":
    print("I prefer to be a module and i can also do some tests")
    lst = [i+1 for i in range(5)]
    print(suml(lst))
    print(prodl(lst))
else:
    print("I like to be a module")



