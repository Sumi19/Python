numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(len(numbers))
print(numbers)

###
myList = [] # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)
###
print(
    """ Calculating Sum of all the values stored in mylist
    """)

myList= [10, 1, 8, 3, 5]
print(myList)
total = 0

for i in range(len(myList)):
    total += myList[i]
print("Total=",total)
####
myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)
####
print("Python offers a more convenient way of doing the swapping variables")
var1 = 1
var2 = 2
var1,var2 =var2,var1
print(var1,var2)

####
print("swap the list's elements to reverse their order:")
myList = [10, 1, 8, 3, 5]
print("Mylist =",myList)

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print("Reversed List=",myList, end=" ")

myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)
print()

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
print(lst)
























