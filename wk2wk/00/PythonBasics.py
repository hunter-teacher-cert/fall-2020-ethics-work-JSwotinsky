# Jonathan Swotinsky
# Hunter CS Program - Ethics & Computer Science
# 9/3/20

# This sample Python code illustrates the following:
#
# Defining and using variables
# Defining and calling ("invoking") functions
# Writing a "Hello, world!" script is a good first step...
# Arrays ("lists" in python)
# 2D lists
# Hashmaps ("dictionaries" in python)

def printAMessage():
    message = "Hi, I am a message!"
    print(message)

def printList(x):
    for i in x:
        print(i, end = "");
    print()

print("Hello, World!")
printAMessage()
myList = ["Hello, ", "World!"]
printList(myList)

myList2 = [[1,2,3],[1,2,3],[1,2,3]]
for i in range(3):
    for j in range(3):
        print(myList2[i][j], end = "")
    print()

myDictionary = {"a":"Item 1", "b":"Item 2", "c":"Item 3"}
print(myDictionary["a"])
print(myDictionary["b"])
print(myDictionary["c"])

    
  