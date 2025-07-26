#Defining and declaring and array
arr = [10, 20,30,40,50]
print(arr)

print(arr[0])
print(arr[2])
print(arr[-1])


brands = ["Coke", "Apple", "Totoya"]
print(brands)

# Finding the length of array
num_brands = len(brands)
print(num_brands)
brands.append("Intel") #adding
print(brands)
brands.remove("Coke") #remove
brands.pop(2) #remove
print(brands)

# Modifying element of an array
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)
fruits[1] = "Jambura"
print(fruits)

# Concatenating two arrays
concat = [1, 2, 3]
concat = concat + [4, 5, 6]
print(concat)

# Repeating element
repeat = ["Ayesha"]
repeat = repeat * 5
print(repeat)

# Slicing the array
# Starting index is inclusive and ending index is exclusive
print(fruits[1:4])
print(fruits[:2])
print(fruits[2:])
print(fruits[-3:-1])


# Declaring and defining Multidimentinal Array
muld = [[1,2], 
        [3,4], 
        [5,6], 
        [7,8]]
print(muld)
print(muld[0])
print(muld[2][1])
print(muld[3][0])

