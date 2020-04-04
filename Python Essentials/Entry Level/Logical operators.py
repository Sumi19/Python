# Example 1
var =1
print(var>0, end=" ")
print(var<=0)
print()

#Example 2
i=1
j = not not i
print(i,j)
print()

# Example 3
# bitwise operation
i = 15 # 00000000000000000000000000001111
j = 22 # 00000000000000000000000000010110
print(i & j) # 00000000000000000000000000000110
print()

# logical operation
print(i and j) # doubt why the output is 22 instead of true?
print(not i, end =" ")
print(~ i) #  ~ i = 11111111111111111111111111110000 = -16

x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2
print(a,b,c,d,e,f, end="")


