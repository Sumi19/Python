# return with expression

def happyNewyear(wishes=True):
    print("Three")
    print("Two")
    print("One")
    if not wishes:
        return
    print("Happy New Year!")
happyNewyear()

# return withourt expression
# The return variant is extended with an expression:

def boringFunction():
    return 123

x = boringFunction()

print("The boringFunction has returned its result. It's:", x)


# About none value None
#print(None + 2)

value = None
if value == None:
    print("Sorry your variable does not carry any value")
print()
############################
print("""
if a function doesn't return a certain value using a return expression clause, it is assumed that it implicitly returns None.

Let's test it.

""")
print("""
def empty_return(x,y):
    c = x + y
    return


res = empty_return(4,5)
print(res)
""")
def empty_return(x,y):
    c = x + y
    return
res = empty_return(4,5)
print(res)
print()
def strangeFunction(n):
    if(n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1))
print()
#################
def sumOfList(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
print(sumOfList([5, 4, 3]))
print()
#################################
################################
def fahrenheit(T_in_celsius):
    """ returns the temperature in degrees Fahrenheit """
    return (T_in_celsius * 9 / 5) + 32

for t in (22.6, 25.8, 27.3, 29.8):
    print(t, ": ", fahrenheit(t))
#################################
def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")

Hello("Peter")
Hello()
#######################
def sumsub(a, b, c=0, d=0):
    return a - b + c - d

print(sumsub(12,4))
print(sumsub(42,15,d=10))
#####################################

# function argument as list
print("Function's argument as list")
def sumOfList(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum
print(sumOfList([5,8,13]))
####################################
print("A list be a function result")
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))

#####################################
print("""Psuedo code:
    if year is divisible by 4 then is_leap _year
else not_leap_year""")
def isYearLeap(year):
    if year% 400 ==0 or (year%4==0 and year%100!=0):
       return True
    return False    

print("""
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]""")
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
##########################################
# write and test a function which takes two arguments (a year and a month)
#and returns the number of days for the given month/year pair
#(while only February is sensitive to the year value,
#your function should be universal).

def isYearLeap(year):
    if year% 400 ==0 or (year%4==0 and year%100!=0):
        return True
    return False
    
def daysInMonth(year, month):
    if isYearLeap(year) == True and month == 2:
        return 29
    elif isYearLeap(year) == False and month == 2:
        return 28
    elif month%2 == 0:
        return 30
    
    return 31
print("""
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]""")

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 10]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
#######################################

def isYearLeap(year):
    if year% 400 ==0 or (year%4==0 and year%100!=0):
        return True
    return False
    

def daysInMonth(year, month):
    if isYearLeap(year) == True and month == 2:
        return 29
    elif isYearLeap(year) == False and month == 2:
        return 28
    elif month%2 == 0:
        return 30
    return 31

def dayOfYear(year, month, day):
    return day

print(dayOfYear(2000, 12, 31))
###########################################################
print("Finding the day of the week given the date")
def isYearLeap(year):
    if year% 400 ==0 or (year%4==0 and year%100!=0):
        return True
    return False
    

def daysInMonth(year, month):
    month30 = [4,6,9,11]
    month31 = [1,3,5,7,8,10,12]
    if month == 2:
       if isYearLeap(year)== True:
           return 29
       return 28
    for m in month30:
        if month == m:
            return 30
    for m in month31:
        if month == m:
            return 31
print(daysInMonth(1900, 9))

def isValidDate(year, month, day):
    
    if year<1800 or year>2200:
        return "Invalid"
    elif daysInMonth(year, month) == 29 and day>29:
        return "Invalid"
    elif daysInMonth(year, month) == 28 and day>28:
        return "Invalid"
    elif daysInMonth(year, month) == 30 and day>30:
        return "Invalid"
    elif daysInMonth(year, month) == 31 and day>31:
        return "Invalid"
    else:
        return "Valid"
print(isValidDate(1900, 4, 31))
print(isValidDate(2000, 12, 31))

import calendar

d=dict(enumerate(calendar.day_name))
print(d)

import datetime

def dayOfYear(year, month, day):
    if isValidDate(year, month ,day) == "Valid":
        print("The day is",end =" ")
        d = datetime.date(year, month, day)        
        return d.weekday()
    return "Enter Valid date"
    
print(dayOfYear(1900, 4, 31))
print(dayOfYear(2000, 12, 31))
print(dayOfYear(1900, 2, 28))

############################################
print("Finding prime Numbers")
def isPrime(num):
    if num >1 :
        for i in range(2,num):
            if num%i == 0:
                return False
        return True
    return False
    

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()
###########################################
print("""
A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

Your task is to write a pair of functions converting l/100km into mpg, and vice versa.
1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
"""
)
def l100kmtompg(liters):
  gallon = liters/3.785411784
  mpg = 100/1.609344 
  return(mpg/gallon)

def mpgtol100km(miles):
  km = miles * 1.609344
  return((3.785411784/km)*100)

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))




































    

