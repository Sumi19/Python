# Write a program which reads one natural number and
#executes the above steps as long as c0 remains different from 1.
# We also want you to count the steps needed to achieve the goal.
# Your code should output all the intermediate values of c0, too.



c0 = int(input ("Enter any Non zero or Non Negative integer"))
counter = 0
while c0!= 1:
    counter += 1
    if c0 % 2 == 0:
        c0 = int(c0/2)
    
    else:
        c0 = int(3 * c0 + 1)
    
    print(c0)
    
        
print("There are", counter, "steps")
