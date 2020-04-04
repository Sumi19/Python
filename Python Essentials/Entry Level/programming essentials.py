# Example 1
#while True:
   # print("Stuck in an infinite loop.")
#println()

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
print()

# Example 3
word = "Python"
for letter in word:
    print(letter, end="*")
print()

# Example 4
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
print()

#example 5
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
print()

# Example 6
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
print()

#Example 7
n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")
print()

#Example 8
for i in range(3):
    print(i, end=" ")
print()

for i in range(6, 1, -2):
    print(i, end=" ")
print()
#Example 10
# Create a for loop that counts from 0 to 10
# prints odd numbers to the screen. 
for i in range(0,10):
    if i%2 == 1:
        print(i, end =" ")
print()

# Example 11
#Create a while loop that counts from 0 to 10
# prints odd numbers to the screen.
i = 0
while i <= 10:
    if i%2 !=0:
        print(i, end = ",")
    i += 1
print()

# Example 12
# Create a program with a for loop and a break statement.
# The program should iterate over characters in an email address,
# exit the loop when it reaches the @ symbol, and
# print the part before @ on one line.

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
print()

#Example 13
# Create a program with a for loop and a continue statement.
# The program should iterate over a string of digits, replace each 0 with x
# print the modified string to the screen.

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    else:
        print(digit, end ="")
print()

# Example 14
n = range(4)
for num in n:
    print(num - 1,end=" ")
else:
    print(num)
print()

#Example 15
n = 3
while n > 0:
    print(n + 1, end =" ")
    n -= 1
else:
    print(n)


     


        
