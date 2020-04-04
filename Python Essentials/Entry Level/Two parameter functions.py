print("Two Parameter functions")
print()
############################################################

print("--------------------------------------------------")
print("A function to evaluate the Body Mass Index (BMI).")
def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))
print()

#################################################################

print("---------------------------------------------------------------------")
print("Program to evaluate BMI and converting imperial units to metric units")
def lbstokg(lb):
    return lb * 0.45359237   # 1 lb = 0.45359237 kg.

print(lbstokg(1))

def ftintom(ft, inch=0.0):   #1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m.
    return ft * 0.3048 + inch * 0.0254

print(ftintom(1, 1))

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(352.5, 1.65))
print(bmi(weight = lbstokg(176), height = ftintom(5, 7)))

print()
##############################################################################
print("---------------------------------------------------------------------")
print("a function to check whether three sides of given lengths can build a triangle.")
def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

def isItATriangle(a, b, c):
    if a + b <= c or b + c <= a or c+a <= b:
        return False
    return True

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

print()
################################################################################
print("---------------------------------------------------------------------")
print()
print(" Triangles and the Pythagorean theorem")
print("""Program to  test the relationship between the hypotenuse and the remaining sides
we choose the longest side, and apply the Pythagorean theorem to check if everything is right.""")

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
else:
    print("Sorry, it won't be a triangle.")

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
       return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
                 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2    
    if b> a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    
#print(isItRightTriangle(5, 3, 4))
#print(isItRightTriangle(1, 3, 4))
print(isItATriangle(a, b, c))    
print(isItRightTriangle(a, b, c))
print()
################################################################################
print("---------------------------------------------------------------------")
print("Heron's formula - evaluating a triangle's field")
def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
else:
    print("Sorry, it won't be a triangle.")

def heron(a, b, c):
    s = (a + b + c) /2
    return (s * (s - a) * (s- b) * (s - c)) ** 0.5
    

def fieldOfTriangle(a, b, c):
    if not isItATriangle(a,b,c):
        return None
    return heron(a,b,c)

print(fieldOfTriangle(1., 1., 2.**.5))
print(fieldOfTriangle(a, b, c))
print()

################################################################################
print("---------------------------------------------------------------------")
print("Factorials")
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): # testing
    print(n, factorialFun(n))
print(8,factorialFun(8))

print()
####################################################################################
print("---------------------------------------------------------------------")

print("Fibonacci numbers")
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))


print()
################################################################################
print("---------------------------------------------------------------------")
print("Recursion -- A technique where a function invokes itself.")
print("Fibonacci")
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
for n in range(1, 10):
    print(n, "->", fib(n))
print()
print("Factorial")
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)
for n in range(1, 6): # testing
    print(n, factorialFun(n))
print(8,factorialFun(8))
print()
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))





      
