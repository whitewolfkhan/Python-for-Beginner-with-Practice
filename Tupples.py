# Tupples is similar to list. we cannot change the element of a tuple once it is assigned, but in list it can changed.
# that means , list is mutable and tupple is immutable. 
# Advantage :           1. use tuple for heterogenous different data types
#                       2. iterating through the tuple is faster
#                       3. can be used as key for a dictionary

tuple1 = ()
print(tuple1)

tuple2 = (1,2,3)
print(tuple2)

# creating tuple differnet datatypes
tuple3 = (101, "Meheer", 234.3, "a")
print(tuple3)

#creation a nested tuple
tuple4 = ("points", [1,2,3], (4,5,6)) # (string, list, tuple)
print(tuple4)

tuple5 = 101, "Jisan", 20000.20, "Hr dept"
print(tuple5)

#tuple unpacking 
empid,empname,empsal,empdept = tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)

print(type(tuple5))


#accessing tuple
print(tuple4)
print(tuple4[0])
print(tuple4[1][2])


#slicing
tuple6 = ('w','e','1','3','m','f','e')

print(tuple6[1:3])
print(tuple6[:3])


#tuple elements are immutable
#tuple6[2] = 'x'  #error

#concatation of tuple
print(tuple6 + tuple5)
print(("again",)* 4)

#delation not happen .
#but can delete entire tuple
# del tuple6



#tuple methods
print(tuple6.count('e'))
print(tuple6.index('m'))

#operation , membership
print(tuple6)
print('e' in tuple6)
print('k' in tuple6)


#iteration through tuple elements
for letters in tuple6:
    print("letters is ->" , letters)
    

#built in function in tuple
tuple7 = (22,33,11,56,78,65,99)
print(tuple7)

print(max(tuple7))
print(min(tuple7))
print(sorted(tuple7))
print(len(tuple7))
print(sorted(tuple6))




