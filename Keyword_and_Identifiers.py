# true and false
print(5 == 5)
print(5<5)

# None
def a_void_function():
    a = 1
    b = 2
    c = a + b

x = a_void_function()
print(x)

# and, or, not
print(True and False)
print(True or False)
print(not False)

# assert
# if false , here occur AssertationArror
assert 6 > 4
assert 4 == 4 

# break
for i in range(1,11): # 1 to 10
    if i == 5:
        break
    print(i)
    

# continue
for i in range(1,8): # 1 to 10
    if i == 5:
        continue
    print(i)
    

# class
class ExampleClass:
    def f1(parameters):
        print("this is function1")
    def f2(parameters):
        print("this is function2")
        
obj1 = ExampleClass()
obj1.f1()
obj1.f2()


# def ( it is used when i am going to define user defined function)
def funName(parametes):
    pass # not output will be obtained
funName(10)


# try...raise....catch....finally
try:
    x = 9
    raise ZeroDivisionError #(we pretend this error can occur)
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Execution succesfully")



# Global
globval = 10
def read1():
    print(globval)
def write1():
    global globval
    globval = 5
def write2():
    globval = 15 # this is now local variable
    
read1()
write1()
read1()
write2()
read1()


# in , not in(in and not in used for membership)
a = [1,2,3,4]
print(4 in a)
print(44 in a)
print(4 not in a)
print(44 not in a)


# lambda (defined anonymous function that is user defined function, no name for this function)
a = lambda x: x*2
for i in range(1,7):
    print(a(i))
    

#nonlocal
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("inner function: ", a)
    inner_function()
    print("outer function: ", a)
outer_function()


# with
with open('example.txt', 'w') as myfile:
    myfile.write('Hello world')



# yield (instead of having that 'return' , in generative functions will be having the keyword yield which will go on accumulating all the calculated values)
# iterator 
def generator():
    for i in range(6):
        yield i*i
    
g = generator()
for i in g:
    print(i)