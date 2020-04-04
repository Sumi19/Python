print(
        """
the name of an ordinary variable is the name of its content;
the name of a list is the name of a memory location where the list is stored.
        """)
list1 = [1]
list2 = list1
list1[0] = 2
print(list2)
##########################

#A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
#It actually copies the list's contents, not the list's name.
print("Powerful slices")
# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

############################
print("Slices-Negative indices")
newList = myList[1:-1]
print(newList)

print(
    """If the start specifies an element lying further than the one described by
the end , the slice will be empty:""")
newList = myList[-1:1]
print(newList)

newList = myList[:3]
print(newList)

newList = myList[3:]
print(newList)

################################
print("Slices-del")
myList = [10, 8, 6, 4, 2]
print("del instruction is able to delete more than just a list's element at once - it can delete slices too:")
del myList[1:3]
print(myList)


myList = [10, 8, 6, 4, 2]
print("Deleting all the elements at once ")
del myList[:]
print(myList)


myList = [10, 8, 6, 4, 2]
print("The del instruction will delete the list itself, not its content.")
del myList
#print(myList)
###############################

print("Slices- in and not in operators")
myList = [0, 3, 12, 8, 2]

print(5 in myList)
print(5 not in myList)
print(12 in myList)

###################################################
print("Finding the largest number")
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]

print(largest)

for i in myList:
    if i > largest:
        largest = i

print(largest)


for i in myList[1:]:
    if i > largest:
        largest = i

print(largest)
###############################################
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5
#found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

print("Lottery")
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)
####################################################

print("a program which removes all the number repetitions from the list. ")
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist = []
for i in myList:
    if i not in newlist:
        newlist.append(i) 
print("The list with unique elements only:")
print(newlist)










