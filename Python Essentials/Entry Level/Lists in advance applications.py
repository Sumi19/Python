print("List Comprehension")
print("""
    The part of the code placed inside the brackets specifies:
        The data to be used to fill the list
        The clause specifying how many times the data occurs inside the list (for i in range())
      """)


squares = [x ** 2 for x in range(10)]
print(squares)
twos = [2 ** i for i in range(8)]
print(twos)
odds = [x for x in squares if x % 2 != 0 ]
print(odds)
cubed = [num ** 3 for num in range(5)]
print(cubed) 


################################################
# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. 
#There are 20 rooms on each floor.
#Create an array which can collect and process information on the occupied/free rooms.


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# book a room for two newlyweds: in the second building, 
# on the tenth floor, room 14:

rooms[1][9][13] = True
# release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building:
vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1
print(vacancy)
print(rooms)

###############################
#You can use nested lists in Python to create matrices
#(i.e., two-dimensional lists). For example:
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)

###################################
# Cube - a three-dimensional array (3x3x3)
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
################
print("Quiz")
print()

l = [ 0 for i in range(1,2)]
print(l)
print()
###############
i =2
while i >=0:
    print("x",end="")
    i-=2
print()
#################
for i in range(-1,1):
    print("#", end="")
print()
################
z=10
y=0
x=z>y or z==y
print(x)
print()
###########
lst = [3,1,-1]
lst[-1]=lst[-2]
print(lst)
print()
#################
nums =[]
vals = nums
vals.append(1)
print(vals, nums)
#################
nums = []
vals = nums[:]
vals.append(1)
print(vals , nums)
########################
lst = [0,1,2,3]
x=1
for elm in lst:
    x*= elm
print(x)
vals=[0,1,2]
print(len(vals))
vals[0],vals[1]=vals[1],vals[2]
print(len(vals))

























        
























