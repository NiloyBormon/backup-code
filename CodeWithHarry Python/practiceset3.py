# Create a string variable name with your full name. Print:
# The first character
# The last character
# The length of the string
# Concatenate two strings: "Hello" and "World" with a space in between.

# sol:
# name = "niloy bormon"
# print(name[0])
# print(name[-1])
# print(len(name))

# # sol:
# str1= "Hello"
# str2= "World"
# print(str1+" "+str2)

# Given text = "Python Programming", do the following:
# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string
# Reverse the string text using slicing.

# text = "Python Programming"
# for i in range (6):
#     print(text[i],end=" ")
# print()

# for i in range (-1,-7,-1):
#     print(text[i])

# for i in range (1,len(text),2):
#     print(text[i])

# a = len(text)
# for i in range (a-1,-1,-1):
#     print(text[i])

# Take the string "  i love python programming  " and:
# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears
# Check if the string "123abc" is alphanumeric.

# text = "  i love python programming1  "
# print(text.strip())

# print(text.title().strip())

# count = 0
# for i in range(0,len(text)):
#     if(text[i]=='o'):
#         count += 1
# print(count)

# text = "abc5"
# print(text.isalnum())

# Using format(), create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.
# Do the same using f-strings.

# text = "My name is {}, My cgpa is {}"
# a = input("Enter your name:")
# b = input("Enter your cgpa:")
# print(text.format(a,b))
# print(f"My name is {a}, My cgpa is {b}")

# Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
# Find the index of the word "Python" in sentence.
# Convert the entire sentence to uppercase and print it.

# text = "Coding in Python is fun"
# print(text.replace("fun","awesome"))

# print(text.index("Python"))

# print(text.upper())

# text = input("enter a text:")
# length = len(text)
# vowel = ['a','e','i', 'o','u']
# count = 0
# for i in range (length):
#     if text[i] in vowel:
#         count += 1
# print("the num of voules is: ",count)

# text = input("Enter a scentence:")
# a = len(text)
# isPalindorm = True
# for i in range(a):
#     if text[i]!= text[a-1-i]:
#         isPalindorm = False
# print(isPalindorm)

def fib(n):
    start =0
    secnd = 1
    
num = input("enter a number:")
