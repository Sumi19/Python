# This function uses global variable s 
def f():  
    print(s)  
  
# Global scope 
s = "I love Geeksforgeeks"
f() 
##############################################################
print("""A variable existing outside the function has a scope
      inside the function's bodies""")
def myFunction():
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)
##############################################
print("""A variable existing inside the function has no scope
      outside the function's bodies""")
def scopeTest():
    x = 123

scopeTest()
#print(x)
################################
print(""" If a variable with same name is defined inside the scope of function
as well then it will print the value given inside the function only
and not the global value.""")
# This function has a variable with 
# name same as s. 
def f():  
    s = "Me too."
    print(s)  
  
# Global scope 
s = "I love Geeksforgeeks" 
f() 
print(s)
print()



print(""" the scope of a variable existing outside a function is supported only
    when getting its value (reading).
    Assigning a value forces the creation of the function's own variable.""")
def myFunction():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)
###########################################
print("""Program to to show, there is no need to use global keyword for accessing global variable""")
a=15
b=10
def add():
    c=a+b
    print(c)
add()
#####################################################
print(""" Program to modify a globalvalue without using global keyword""")
a=15
def change():
    a=a+2
    print(a)
#change()
#######################################
print("""Program to modify a global variable using inside a function using global keyword""")
    
x=15
def change():
    global x
    x=x+5
    print("Value inside the function", x)
change()
print("Value outside the function", x)
############################################
print("""program showing a use of global in nested function """)
  
def add(): 
     x = 15
       
     def change(): 
         global x 
         x = 20
     print("Before making changing: ", x) 
     print("Making change") 
     change() 
     print("After making change: ", x) 
  
add() 
print("value of x",x)
#######################################
print()
print("This function modifies global variable 's' ")
def f(): 
    global s 
    print (s) 
    s = "Look for Geeksforgeeks Python Section"
    print (s)
  
# Global Scope 
s = "Python is great!" 
f() 
print (s)
print()
#############################################
a = 1
  
# Uses global because there is no local 'a' 
def f(): 
    print 'Inside f() : ', a 
  
# Variable 'a' is redefined as a local 
def g():     
    a = 2
    print 'Inside g() : ',a 
  
# Uses global keyword to modify global 'a' 
def h():     
    global a 
    a = 3
    print 'Inside h() : ',a 
  
# Global scope 
print 'global : ',a 
f() 
print 'global : ',a 
g() 
print 'global : ',a 
h() 
print 'global : ',a 

        
    






































