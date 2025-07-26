# For open file
#   'r','w','a (append)','r+ (read and write)'
# reading files :  .read() , .readline(), .readlines()
# writing files : .write() {expects a string}, .writelines() {expects a list}
# with statement : ensures that, opened file are properly closed after the operations, even if exception occurs

# with open("sample.txt", "w") as file:
#     file.write("Hello world\n")
#     file.writelines(["Meheer", "Ali", "Khan"])


# use exception handaling
# FileNotFoundError, PermissionError, IOError
# try:
#     with open("sample1.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found")   
    

# count word and line in a file     
# def countWordAndLine(filename):
#     try:
#         with open("sample.txt", "r") as file:
#             lines = file.readlines()
#             lineCount = len(lines)
#             wordCount = sum(len(line.split()) for line in lines)
            
#             print(f"Number of line : {lineCount}" )
#             print(f"Number of word count : {wordCount}")
#     except FileNotFoundError:
#         print("File not found")
        
# countWordAndLine("sample.txt")



# write and read a list of items
# def writeItem(filename,items):
#     with open(filename, "w") as file:
#         for item in items:
#             file.write(item + "\n")
                
# def readItem(filename):
#     try:
#         with open(filename, "r") as file:
#             items = file.readlines()
#             print("Items in the file")
#             for item in items:
#                 print(item.strip())
#     except FileNotFoundError:
#         print(f"this {filename} not found")
        
# fruits = ["apple", "banana", "dates", "mango"]
# writeItem("fruits.txt", fruits)
# readItem("fruits.txt")



# Copy content one file to another
# with open("fruits.txt", "r") as file:
#     content = file.read()

# with open("desti.txt", "w") as files:
#     files.write(content)
    
# print("Copied succesfully")



# count the number of occurences of a specific word in a text file
# def countWord(filename, item):
#     with open(filename, "r") as file:
#         content = file.read()
#         return content.split().count(item)
    
# filename = "fruits.txt"
# words = "apple"
# count = countWord(filename, words)
# print(f"The word {words} appears {count} times")



# log messages with timestamps into a file
import logging  # used to record messages, errors, warnings, and debug info, especially helpful for debugging and tracking program behavior over time.

logging.basicConfig(
    filename="app.log",
    level= logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S"
)


logging.info("Program started")
logging.info("program some task")
logging.info("program ended")
