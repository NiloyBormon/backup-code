# Write a function greet() that prints "Hello, Python Learner!" when called.
# Write a function square(num) that returns the square of a given number. Test it with different numbers.

# def greet():
#     print("Hello, Python Learner!")
# greet()

# def square(num):
#     return num * num
# num = int(input("enter a number:"))
# print(square(num))

# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)

# def full_name(first, last):
#     print(first,last)

# first = input("enter your first name:")
# last = input("enter your last name:")
# full_name(first,last)

# def calculate_area(length, width=10):
#     return length*width

# length = int(input("enter length:"))
# # width = int(input("enter width:"))
# print(calculate_area(length))

# Write a lambda function that adds two numbers and test it.
# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.


# add = lambda x,y : x+y
# print(add(5,6))

# square = lambda num: num*num
# lst = [1, 2, 3, 4, 5]
# for i in lst:
#     print(square(i))

# using map()
# lst = [1, 2, 3, 4, 5]
# square = list(map(lambda x : x*x,lst))
# print(square)

# Write a recursive function factorial(n) that returns the factorial of a number.
# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

# def factorial (number):
#     if number== 0 or number == 1:
#         return 1
#     else :
#         return factorial(number-1)*number
# print(factorial(6))

# def sum_of_digits(n):
#     if n == 0:
#         return n
#     else:
#         return (n%10)+sum_of_digits(int(n/10))
# print(sum_of_digits(897))

# Import the math module and use it to:
# Find the square root of 144
# Calculate sin(90°) (hint: use math.radians())
# Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".

# import math 
# print(math.sqrt(144))

# print(math.sin(90))

# import requests
# x = requests.get("https://api.github.com")
# print(x.text)

# Bonus Challenges
# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.
# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else :
#         return fibonacci(n-2) + fibonacci(n-1)
# print(fibonacci(7))