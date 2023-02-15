## Exercise 1: Introducing the list data type
# Defining a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print("This list has {} fruits".format(len(myFruitList)))

# Accessing a list by position
print("Fruits in this list are:")
for fruit in range(len(myFruitList)):
    print(myFruitList[fruit])

# Changing the last value in a list
prevLastFruit = myFruitList[-1]
myFruitList[-1] = "orange"
print("Previous fruit,", prevLastFruit,
 "at end of the list, is changed to", myFruitList[-1])

## Exercise 2: Introducing the tuple data type
# Defining a tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print("This tuple has {} fruits".format(len(myFruitList)))

# Accessing a tuple by position
print("Fruits in this tuple are:")
for fruit in range(len(myFinalAnswerTuple)):
    print(myFinalAnswerTuple[fruit])

## Exercise 3: Introducing the dictionary data type
# Defining a dictionary
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
    }
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print("Contents in this dictionary are", myFavoriteFruitDictionary)

# Accessing a dictionary by name and by fruit
tempKeyList = [*myFavoriteFruitDictionary] # Method: [*dict] to extract keys
# tempKeyList = list(myFavoriteFruitDictionary.keys()) # Method: List func + keys method
print("This dictionary has {} names".format(len(tempKeyList)))
print("The names in this dictionary are:")
for name in range(len(tempKeyList)):
    print(tempKeyList[name])

tempValueList = [*myFavoriteFruitDictionary.values()] # Method: [*dict] to extract values
# tempValueList = list(myFavoriteFruitDictionary.values()) # Method: List func + keys method
print("This dictionary has {} fruits".format(len(tempValueList)))
print("The fruits in this dictionary are:")
for fruit in range(len(tempValueList)):
    print(tempValueList[fruit])
