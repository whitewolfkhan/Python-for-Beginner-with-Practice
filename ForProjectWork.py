# best practie:  1. use descriptive variable names
#                2. write moduler code with functions and classes
                #  3. Follow PEP 8 (in github) style guidelines
                #  4. avoid redundancy; leverage pythons powerfull built in function
# List Comprehensions : A concise way to create lists using a single line of code
# create a list of square
squares = [x**2 for x in range(10)]
print(squares)

# Filter even number
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Lambda : anonymous funtion , single expression function
add = lambda x, y : x + y
print(add(3,5))

# map : applies a function to each item in an iterable
num = [1,2,3,4]
sq = map(lambda x: x**2, num)
print(list(sq))

# filter : Filters items based on a condition
evenlist = filter(lambda x: x % 2 == 0, num)
print(list(evenlist))

#reduce: reduce an iterable to a single value
from functools import reduce
product = reduce(lambda x,y: x*y, num)
print(product)