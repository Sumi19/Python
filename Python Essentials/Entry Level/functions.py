def message():
    a = int(input("Enter a start value: "))
    b = int(input("Enter a end value: "))
    print("We start here at ", a)
    print("We end here at", b)

message()
#############################
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
print(a,b,c)
###########################
def myFunction(a, b, c):
    print(a, b, c)

myFunction(1, 2, 3)
#####################
def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
##################################

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
#####################################

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke")
#########################
def sum(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# call the sum function here
sum(1, 2, 3) #a pure example of positional argument passing.
sum(c = 1, a = 2, b = 3)# purely keyword variant
sum(3, c = 1, b = 2) #Mixing positional and keyword arguments
#sum(3, a = 1, b = 2) # typeError

##################################
def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)

# call the function here
introduction("James", "Doe")
introduction("Henry")
introduction(firstName="William")

def introduction(firstName="John", lastName="Smith"):
    print("Hello, my name is", firstName, lastName)
introduction()
introduction(lastName="Hopkins")
######################
def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)

s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s, c, pC)
##############################################
#Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


#Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

#Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3
#subtra(a=2,5) shows error

#Ex. 4
def sum(a, b=2, c=2):
    print(a + b + c)

sum(1,3,4)
sum(a=1, c=3)
sum(1)
# Ex.5
#SyntaxError - a non-default argument (c) follows a default argument (b=2)
#def sum(a, b=2, c):
#    print(a + b + c)


















































































