class MycomplexNumber:
    #Constractor Method
    def __init__(self, real = 0, imag = 0):
        print("My Complex number constractor is :...")
        self.real_part = real
        self.imag_part = imag
        
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.imag_part))
        
        
#create a new object MyComplexNumnber class
cmplx1 = MycomplexNumber(40,50)

#calling the display function
cmplx1.displayComplex()


# Create another object against MycomplexNumber class
# and create a new attribute 'new_attribute'
# (Note: cmplx1 cannot create new attribute)
cmplx2 = MycomplexNumber(60,70)
cmplx2.new_attribute = 80
print(cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute)

#deleting 
print(cmplx1)
del cmplx1.real_part
del cmplx1

print(cmplx1)

