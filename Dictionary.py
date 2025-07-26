# Python dictionary is an unordered collection of items, and while other compound data types have only
# the value as an element, but in of dictionary will be having our key value pair and dictionaries are
# optimized to retrieve values when the key is known to us.

#accessing elementes from a dicstionary
# newDict = {1:"Hello", 2:"Hi", 3:"Ayesha"}
# print(newDict)
# print(newDict[1])  # if we write newDict[10], it will show key error
# print(newDict.get(1)) # if we write newDict[10], not show any error

# #updating value
# newDict[1] = "Hey"
# print(newDict)

# #add
# newDict[4] = "Assalamualaikum"
# print(newDict)

# squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(squares)

# #remove a particuler item
# print(squares.pop(4))
# print(squares)

# #remove a arbitrary item
# print(squares.popitem())
# print(squares)

# #delete a particular item
# del squares[1]
# print(squares)



# Creating a new dictionary using Comprehension
squares = {x: x*x for x in range(6)}
print(squares)

#membership test (membership test for key only, not value)
print(1 in squares)


#iterate
for i in squares:
    print(squares[i]) # value print

# {build in function (len, sorted)}



# word frequency counter
# sentence = input("Enter a string :")

# #split the sentene
# words = sentence.split()

# #initialize dictionary
# wordCount = {}

# #count
# for word in words:
#     word = word.lower()
#     if word in wordCount:
#         wordCount[word] += 1
#     else:
#         wordCount[word] = 1
# print(wordCount)



#store student grade in a dictionary and calculate the average grade
grades = {"meheer":56,"ali":67,"khan":89, "ayesha":73, "akter": 99}

average = (sum(grades.values()))/len(grades)

print("Student grades : ", grades)
print("Average of students : ", average)