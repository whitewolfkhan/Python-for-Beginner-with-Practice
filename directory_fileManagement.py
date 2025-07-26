# os module : Provide functions to interact with the operating system

import os
print(os.getcwd()) # return the current working directory
print(os.getcwdb()) # return the current working directory as a byte object


os.chdir('G:\\PythonPractice\\FileTest') # use to change directory
print(os.listdir()) # all files in this directory can be known(show) using listdir()
print(os.getcwd())

#used to make a new directory
#os.mkdir('Test')

# rename a directory
#os.rename('Test', 'newOne')

#removing a file and directory
# os.remove('one.txt')
# os.rmdir('Test')

os.chdir('G:\\PythonPractice') # return original directory



# sys module : Provide access to system specific parameters and functions
import sys

print(sys.argv)
print(sys.version)