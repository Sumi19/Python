tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125
print(tuple1)
print(tuple2)
oneElementTuple1 = (1, )
oneElementTuple2 = 1., 
print(oneElementTuple1)
print(oneElementTuple2)
print()

# Example 1
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

# Example 2
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

# Example 3
t3 = (1, 2, 3, 5)
print(len(t3))

# Example 4
t4 = t1 + t2
t5 = t3 * 2

print(t4)
print(t5)



print("Getting elements in a tuple")
print("---------------------------------------------")
myTuple = (1, 10, 100, 1000)

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-2])

for elem in myTuple:
    print(elem)
print()



print("Instructins causing runtime error in tuples but not in the list")
print("----------------------------------------------------------------")
print("""#myTuple.append(10000)
#del myTuple[0]
#myTuple[1] = -10
""")
print()


print("""Using len() "+" and "*" operators, 'in' and 'not in' in tuples""")
print("-------------------------------------------------------------------")
myTuple = (1, 10, 100)

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)
print()

print("""Tuples elements ca nbe variables and expressions
(if they are on the right side of the assignment operator)""")
print("---------------------------------------------_______________")
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
print()

print("Dictionaries")
print("--------------")

dictry = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}

print(dictry)
print(phoneNumbers)
print(emptyDictionary)
print()

print("To get the values in the dictionary using valid key")
print("-----------------------------------------------------")
print(dictry['cat'])
print(phoneNumbers['Suzy'])
print()
print("runtime error")
print("""phoneNumbers['president']""")
#print(phoneNumbers['president'])
print()

print("""Using 'in' or 'not in' to avoid runtime error""")
print("------------------------------------------------")
dictry = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictry:
        print(word, "->", dictry[word])
    else:
        print(word, "is not in dictionary")

print()
print("""Building a temporary link between dictionary and a temporary seqence
using method named keys(), items(), values()""")
print("----------------------------------------------------------------------")
dic = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for key in dic.keys():
    print(key, "->", dic[key]) # returns list of keys

for english, french in dic.items(): # returns list of tuples(key-value pair)
    print(english, "->", french)

for french in dic.values(): #returns list of values
    print(french)

print()
print("Modifying dictionaries by adding , inserting , deleting items")
print("--------------------------------------------------------------")
dic = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
print()

dic['cat'] = 'minou' # replacing value
print(dic)

dic['swan'] = 'cygne' # adding new item
print(dic)

dic.update({"duck" : "canard"}) # inserting a new item
print(dic)

del dic['dog']  # removing an item
print(dic)

dic.popitem()   # removing the last item
print(dic)

print()
print("Tuples and dictionaries can work together")
print("--------------------------------------------------------------")
print("""you need a program to evaluate the students' average scores;
the program should ask for the student's name, followed by her/his single score;
the names may be entered in any order;
entering an empty name finishes the inputting of the data;
a list of all names, together with the evaluated average score,
should be then emitted.""")
schoolClass = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    
    if name in schoolClass:
        schoolClass[name] += (score,)
    else:
        schoolClass[name] = (score,)
        
for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)

print()

print("Modifying dictionaries")
print("-----------------------")
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }
polEngDict.update({'kwait':'flower'})
polEngDict.update({'yes':'no'})
print(polEngDict)
for item in polEngDict:
    print(item)

print()
print("""Write a program that will "glue" the two dictionaries
(d1 and d2) together and create a new one (d3).""")
print("--------------------------------------------------------")
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)


polEngDict = {'zamek': 'castle', 'woda'  : 'water','gleba' : 'soil'}
polEngDict.update({'kwait':'flower','yes':'no'})

d4={}
for item in (polEngDict,d3):
    d4.update(item)
print(d4)
print()

print("Write a program that will convert the colors tuple to a dictionary.")
print("-------------------------------------------------------------------")
colors = (("green", "#008000"), ("blue", "#0000FF"))

colDict = dict(colors)
print(colDict)









































