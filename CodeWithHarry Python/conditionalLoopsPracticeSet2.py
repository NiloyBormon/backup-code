# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
# Create a program that checks if a person is eligible to vote (age >= 18).
# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

# sol1:
# number = int(input("Enter any number: "))
# if number<0:
#     print("the number is negative")
# elif number==0:
#     print("the number is zero")
# else:
#     print("number is positive")

# sol2:
# age = int(input("enter your age:"))
# if age>=18:
#     print("you are eligable to vote")
# else:
#     print("you are not eligable to vote")

# sol3:
# number = int(input("enter a number:"))
# if number%2==0:
#     print("the numver is even")
# else:
#     print("number is odd")

# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
# Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

# sol:
# dayNum = int(input("enter a day number:"))
# match dayNum:
#     case 1:
#         print("sunday")
#     case 2:
#         print("monday")
#     case 3:
#         print("tuesday")
#     case 4:
#         print("wednesday")
#     case 5:
#         print("thursdayu")
#     case 6:
#         print("friday")
#     case 7:
#         print("saturday")
#     case _:
#         print("u entered a invalid number")

# sol2:
# num1 = int(input("enter first number:"))
# num2 = int(input("enter secound number:"))
# op= input("enter the desiared opreator:")
# match op:
#     case '+':
#         print("the sum of two numbers are ",num1+num2)
#     case '-':
#         print("the sub of two numbers are ",num1-num2)  
#     case '*':
#         print("the mul of two numbers are ",num1*num2)
#     case '/':
#         print("the div of two numbers are ",num1/num2)
#     case _:
#         print("you did not enter a valid operator!")

# Print numbers from 1 to 10 using a for loop.
# Print the multiplication table of a number (entered by user).
# Calculate the sum of all numbers from 1 to 100 using a for loop.
# Print the following pattern using a for loop:
# *
# **
# ***
# ****

# sol:
# for i in range(1,11):
#     print(i)

# sol:
# num = int(input("enter a number:"))
# for i in range (1,11):
#     print(f"{num}*{i}={num*i}")

# sol:
# sum = 0
# for i in range(1,101):
#     sum += i
#     # print("sum of all numbers from 1 to 100 is",sum) 
# print("sum of all numbers from 1 to 100 is",sum)

# sol:
# for i in range(5):
#     for j in range(i):
#         print('*',end="")
#     print()

# Print numbers from 1 to 10 using a while loop.
# Write a program that keeps asking the user to enter a password until they enter the correct one.
# Use a while loop to reverse a given number (e.g., 123 → 321).

# sol:
# i =1
# while i<11:
#     print(i)
#     i += 1

# sol:
# password = '12345 '
# typePassword = input("Enter the password: ")
# while typePassword != password:
#     typePassword = input("Your password is wrong!Try again:")

# sol:
# number = input("Enter a number:")
# i =len(number)
# while i-1>0 or i-1==0:
#     print(number[i-1],end="")
#     i -= 1

# Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).
# Print numbers from 1 to 10, skipping the number 5 (use continue).
# Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass)

# sol:
# for i in range(1,11):
#     print(i)
#     if(i==7):
#         break
    
# sol:
# for i in range (1,11):
#     if i==5:
#         continue
#    print(i)

# sol:
# for i in range ( 1,6):
#     if i == 3:
#         pass