import re

# #different ways to define
# st1 = "welcome "
# st2 = 'welcome '
# st3 = '''welcome '''
# print(st1,st2,st3)

# st4 = """welcome
# to the world of
# python programming"""
# print(st4)


# #accessing
# print(st1[0])
# print(st1[-1])
# print(st1[1:3])

# # String are immutable , but differents strings can be assinged, but inside 
# # a string character cannot change

# #Concatation (Using '+' (add two string))

# #iterating through a string
# letterCount = 0
# for letter in "Meheer":
#     if(letter == 'e'):
#         letterCount += 1
# print(letterCount, "e has come")

# #membership like sets


# #build in function (enumerate, len)
# print("list Enumerate : ", list(enumerate(st1)))
# print("Length : ", len(st1))



# #string formating using escape sequence
# print("tell me what's your name?")
# print('''tell me "what's your name?"''')
# print('tell me "what\'s your name?"')


# print("C:\\Users\\user\\mydata.txt")
# print("ABC written in \x41\x42\x43 (HEX) representation")



# #format() method
# #default(implicit) order
# defaultOrder = "{} {} and {}".format('Today','is','sunday')
# print(defaultOrder)

# #using positional argument
# positionalOrder = "{1} {0} and {2}".format('Today','is','sunday')
# print(positionalOrder)

# #using keyword argument
# keywordArgument = "{t} {i} and {s}".format(t='Today',i='is',s='sunday')

# #formating number
# print("Binary representation of {0} is {0:b}".format(20))
# print("Binary representation of {0} is {0:x}".format(20)) #Hexadecimal

# #formating float
# print("Exponent representation : {0:e}".format(1566.345))

# #round off
# print("Öne third is: {0:3f}".format(1/3))


# #string methods
# print("Good morning to all".lower())
# print("good morning to all".upper())
# print("Good morning to all".find('to'))
# print("Good morning to all".replace('all','everybody'))
# words = st1.split()
# print("|".join(words))

# print("       hello world".strip())



# Reguler Expressions(Its a way to search ,match, and manipulate text based on patterns)
# Using the re module(import re)
# Common functions:
#               1. re.search(pattern,string) {It searches for a pattern in that particuler string}
#               2. re.findall(pattern,string) {find all the pattern}
#               3. re.sub(pattern,replacement,string) {mean substitute, it replaces occurrences of a particuler pattern}

# text = "Contact me at 8373-343-343"
# digit = re.findall(r"\d+", text)
# print(digit)

# updated = re.sub(r"\d", "meheer", text)
# print(updated)



#build a text cleaner
# def cleanText(text):
#     #remove punctuation
#     text = re.sub(r"[^\w\s]", "", text)
#     #remove extra space
#     text = " ".join(text.split())
#     return text

# inputTex = "    Hello world, ??? welcome to python Programming....  "
# cleanedTex = cleanText(inputTex)
# print("Clean text : ", cleanedTex)



#check pallindrom(a word or a sentence)
# def isPallindrom(text):
#     text = "".join(char.lower() for char in text if char.isalnum())
#     return text == text[::-1]

# inputTex = input("Enter a string : ")
# if isPallindrom(inputTex):
#     print(f"{inputTex} is a palindrom")
# else:
#     print(f"{inputTex} isnot a pallindrom")



# Count vowel 
# def countVowels(text):
#     vowel = "aeiouAEIOU"
#     return sum(1 for char in text if char in vowel)  # here 1 is placeholder value that using to count

# inp = input("Enter a string : ")
# print(f"Number of vowels in {inp}", countVowels(inp))


# find and replace all email address in a text
# def replace_emails(text, replacement="EMAIL"):
#     # to match email addresses
#     info = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     return re.sub(info, replacement, text)

# text = "Contact us at support@example.com or sales.team@company.co.uk for more info."

# new_text = replace_emails(text)
# print("Replaced text:", new_text)



# Reverse a word in sentece, not letters
def reverseWords(sentence):
    #not letters
    word = sentence.split()
   # reverse = " ".join(reversed(word)) # not letter
    #reverse = word[::-1] # not letter letter
    reverse = [word[::-1] for word in reversed(word)]
    return reverse
    
inp = input("Enter a string : ")
print("Reverse sentence : ", reverseWords(inp))
