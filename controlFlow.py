#Prime number or not
# num = int(input ("Enter a number: "))

# if num>1:
#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
            
# else:
#     print(f"{num} is not a prime number")
    
    

#Factorial
# num = int(input("Enter a number :"))

# factorial = 1
# i = 1

# if num < 0:
#     print("factorial not possible")
# else:
#     while i<=num:
#         factorial = factorial * i
#         i = i + 1
#     print(f"Factorial of {num} is {factorial}")

# factorial using function
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)
 
# num = int(input("Enter a number :"))   
# def printFactorial(num):
#     result = factorial(num)
#     print(f"The factorial of {num} is : ", result)
    
# printFactorial(num)



# collection
# users = {'Hans': 'active', 'Eleonore': 'inactive', 'Khan': 'active'}

# Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         break
#     else :
#         print(users)



#range example
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#descending by length
# sortedd = sorted(a, key=len, reverse=True)
# print(sortedd)
# #assending by length
# sortedd1 = sorted(a, key=len)
# print(sortedd1)
# #print with length
# sortedd2 = sorted(a, key=len, reverse=True)
# for word in sortedd2:
#     print(len(word), word)
    
    

#break example
# for n in range(2, 15) : #iterate 2 to 15
#     for i in range(2, n): # check n is divisible by any number
#         if(n%i == 0):
#             print(f"{n} equals to {i} * {n//i}")
#             break
#     else:
#         print(f"{n} is a prime number")



#match statement
#A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. 
# This is superficially similar to a switch statement in C
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")
            
# where_is(Point(5,440))
# where_is(Point(0,34))


# find largest number
# numb = [12,34,22,56,43,21]

# largest = numb[0]

# for num in numb:
#     if num > largest:
#         largest = num
        
# print("the largest number is : " , largest)



# driven calculator
# def add(a, b):
#     return a + b
# def substract (a,b):
#     return a - b
# def multifly(a,b):
#     return a*b
# def divide(a,b):
#     if b!= 0:
#         return a/b
#     else: 
#         return "Division cannt happen by 0"
    
# while True:
#     print("/menu")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. exit")
        
#     choice = input("Enter your choices")
    
#     if choice == "5" :
#         print("Existing Program")
#         break
    
#     num1 = float(input("Enter first number")) 
#     num2= float(input("Enter second number"))
        
#     if choice == "1":
#         print("Result: " , add(num1,num2))
#     elif choice == "2":
#         print("Result: " , substract(num1,num2))
#     elif choice == "3":
#         print("Result: " , multifly(num1,num2))
#     elif choice == "4":
#         print("Result: " , divide(num1,num2))
#     else:
#         print("Invalid choice")


num = int(input("Enter a number :"))
def checkNum(num):
    if num%2 == 0:
        return "The number is even"
    else:
        return "the number is odd"
print(checkNum(num))