# Set is an unordered collection of items.
# That means within the items within the members of the set, there is no ordering the elements.
# The items can be in any order and every element must be unique.
# No duplicate elements will be allowed in a set and must be immutable.
# That means those elements cannot be updated, cannot be changed.
# However, the set itself is mutable.
# That means we can add or remove items from a set.
# Sets can be used for to perform the mathematical set operations like our union intersection, symmetric
# difference, etc.



# #creating sets
# my_set1 = {11,22,33,44,66}
# print(my_set1)
# my_set2 = {101, "Meheer", (21,2,34)} # mix datatypes
# print(my_set2)
# my_set3 = {12,23,45,67,67,87}
# print(my_set3) # duplicate not allow


# #set cannot have mutable items
# #myset4 = {1,2,[3,4]} #error (creation of a set from the list as one of the elements is not possible)

# #but we can make set from a list
# myset4 = set([1,2,3,4])
# print(myset4)
# print(type(myset4))

# #make list from a set
# myset5 = list({1,2,3,4})
# print(myset5)
# print(type(myset5))


# #operation on set
# print(my_set1)
# #my_set1[0] # error (doesnot support indexing)
# my_set1.add(97) #add
# print(my_set1)
# my_set1.update([13,35,57]) #add multiple
# print(my_set1)
# my_set1.update([101,102],{103,104,105})
# print(my_set1) # add list and set


# # remove and discard
# # There very big difference between this discard and this remove, is that in
# # case of discard if the element whatever we are passing as input argument is not present, it is not
# # producing any error, but in case of remove it is producing an error and the name of the error is key error.
# print(my_set3)
# my_set3.discard(4)
# print(my_set3) #no error
# #my_set3.remove(4)
# #print(my_set2) #error

# #using pop
# print(my_set3.pop())
# print(my_set3.pop())
# print(my_set3)
# #print(my_set3.clear()) #clear set

# #union
# my_set6 = {12,23,45,67,67,87}
# my_set7 = {11,22,33,44,66}
# print(my_set6 | my_set7)
# print(my_set6.union(my_set7))

# #intersection
# print(my_set6 & my_set7)
# print(my_set6.intersection(my_set7))

# #set difference
# print(my_set6 - my_set7)
# print(my_set6.difference(my_set7))

# #symetric difference(common element is deleted)
# print(my_set6 ^ my_set7)
# print(my_set6.symmetric_difference(my_set7))


# #iterating through a set 
# for letter in set("Welcome"):
#     print(letter)
    
# #build in function (max,min,sort,len)


# # Frozenset
# # But having this frozen set so python frozen set, frozen set is a new class that has the characteristic
# # of a set, but its elements cannot be changed once assigned.
# # So while tuples are immutable, lists and frozen sets are immutable sets here, so we cannot do any
# # kind of update and change on this frozen set.So we know that tuples are the immutable lists and frozen sets are immutable sets here.
    
# myset8 = frozenset([1,2,3,4])
# myset9 = frozenset([3,4,5,6])
# print(myset8)
# print(myset9)
# print(myset8.difference(myset9))
# #myset8.add(19) # error (attribute error)



# reverse a list and remove duplicates using a set
myList = [3,2,4,5,1,6,4,8,1]

reverseList = myList[::-1]

uniqueSet = set(myList)

print("reverse :" , reverseList)
print("uniques", uniqueSet)