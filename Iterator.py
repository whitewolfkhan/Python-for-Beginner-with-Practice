# Iterate like an object . And these object return data
# ourList = [11,23,44,56,76]

# # get an iterator using iter() method
# outIter = iter(ourList)

# print(next(outIter)) # print 11
# print(next(outIter)) # print 23

# # next(obj) is same as calling obj.__next__() method
# print(outIter.__next__()) # print 44
# print(outIter.__next__()) 
# print(outIter.__next__()) 
# print(outIter.__next__()) # this will occur error. cause all iterate complete


#create a custom iterator
class Pow_of_Two:
    '''class to implement an iterator
    of powers of two'''    # known as 'block comment'. it is the first intended statement of our class
    
    def __init__(self, max = 0): # constractor
        self.max = max
        
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
        
print(Pow_of_Two.__doc__)
a = Pow_of_Two(4)
i = iter(a)
print(next(i))
#print(i.__next__()) # this print also can write 
print(next(i))
print(next(i))



#create a infinite custom iterator
class infinite_Iter:
    '''Infinite iterator to return all
    odd numbers'''
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        num = self.num
        self.num += 2
        return num
    
i = infinite_Iter()
a = iter(i)
print(next(a))
print(next(a))
print(next(a))
print(next(a)) # so it has no terminating logic
    