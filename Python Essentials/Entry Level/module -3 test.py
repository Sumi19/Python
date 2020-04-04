print("quiz1: ", end="")
i = 0
while i <= 5:
    i=i+1
    if i % 2 == 0:
        break
    print("*")
        


l =[[0,1,2,3] for i in range(2)]
#print(l[2][0])
##############
print("quiz 3: ",end =" ")
z = 10
y = 0
x = y < z and z>y or y>z and z<y
print(x)
print()
######################
print("Quiz 4: ", end ="")
t= [ [3-i for i in range(3)] for j in range(3)]
print(t, end =" ")
s =0
for i in range(3):
    s += t[i][i]
print(s)
##########################
lst = [i for i in range(-1,2)]
print("Quiz5: ", lst)
print()
##########################
lst1 = [1,2,3]
lst2 = []
for v in lst1:
    lst2.insert(0,v)
print("Quiz6: ", lst2)
print()
######################
lst = [3,1,-2]
print("Quiz7: ",lst[lst[-2]])
print()
######################
a=1
b=0
c=a&b
d=a|b
e=a^b
print("Quiz8: ",c,d,e,c+d+e)
print()
##########################
lst =[1,2,3,4]
print("Quiz9: ",lst[-3:-2])
print()
######################
var=0
print("quiz10: ")
while var<6:
    var += 1
    if var%2 == 0:
       continue
    print("#", end=" ")
print()
##############################
lst = [1,2,3]
for v in range(len(lst)):
    lst.insert(1, lst[v])
print("Quiz11: ",lst)
print()
################################
x=1
x=x==x
print("Quiz12: ",x)
print()
#################################
vals=[0,1,2]
vals.insert(0,1)
del vals[1]
print("quiz13: ",vals)
print()
#################################
print("Quiz14:")
for i in range(1):
    print("#")
else:
    print("#")
###############################
var =1
while var<10:
    print("#", end="")
    var = var << 1





































