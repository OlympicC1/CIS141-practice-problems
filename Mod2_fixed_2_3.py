# Fixed problems from lines 113-150

# From my notes your demo videos :) helpes me greatly!
# just thought you should know :)

# ORDERS OF OPERATION

# print(2+2) Addition
# print(2-2) Subtraction
# print(2*2) Multiplication
# print(2/2)#Division
# print(9//2)#Floor Division
# print(14%4)# Modules The remainder of a number
# print(4**4)# Expoentiation

# Operator  Precedence: Close to PEMDAS
# parentheses > exponent > mutliplication/division/modules > addition/subtraction

# result = 2**(4/2)     #3 * (2 - 4)
# print(result)

#Using same variable on both sides of assignment: augmented assigbnment
# x = 6
# x = 8
# x -= 2
# print(x)

# What types are returned from these operators? ints use (type(in prent.))
#print(5 / 2)) # (float)
#print(5 // 2)

# DEFINITIONS

#Write your code here :-)

# Interger - Whole numbers
#52
#101

# Floats / Real - decimal numbers
#10.5
#6.7

# String anything with "" (Alpha Numeric Text)pieces of text
#"Helllo, World"
#"1234"
#Bellow (Passing in an argument)

#print(type("1234"))
#print(type(52))
#print(type(10.5))

# If you ever want to print use () after print writing inside
# If type use its own (type(56))

#print(type("Hello World!")) check data type by running print type
# Prompt for two numbers

# INPUT AND OTHER FUNCTIONS

# Input, Math, Other Functions
#Help
#help(print)#To assest in function operation

#Input (Always returns a String)
#user_name = input("what is your name?")
#print("Hello,", user_name)
#print (type(user_name))#wrap the type and use perin
#Math Library Functions
#import math
#num = int(input("What number do you want to square root?"))
#print(math.sqrt(num))
#print(type(num))

#Format- this format lesson on F string consruct
#price = 5.50
#print(f"The calulator costs ${price:.2f}.")

# VARIABLES
# Variables to store any data_ pythons convention, everthing is lowercase and use underscore between words_
# This is called snake case

#x = 5
#y = x + 3 #8
#print(x,y)
#variable on the left and data on the right put = in between
#dont need spaces just nicer if to have them- each line runs in sequence
#you can reasign variables to create different values or data types
#x = 10
#print(x,y)
#x = "Hello"
#print(x,y)
#a,b,c = 1,2,3 #multiple assignment
#print(a,b,c)
#x = y = z = 0 #multiple assignment
#print(x,y,z)
#total_score = 500 #snake case uses _ and its lowercase
#TOTAL_SCORE = 1500 #variables are case sensitive
#str1,str2,str3 = "Hello", "Hallo", "Hey"
#print(total_score, TOTAL_SCORE )

#import keyword # This is how check for keywords in python
#print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#total_score = 500

# I have every module so far typed out and added notes as we went along!
# Thank you for taking your time out Lindsey to help! You really are
# helping me learn and i'm sure others, more than you know!!!



# 2. Create a program that prompts for 2 numbers and then outputs the
#addition, subtraction, multiplication, and division of the first number by the second number.
'''
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# arithmetic operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number if second_number != 0 else "undefined"

# results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

'''
# 3. Create a program that prompts for the side lengths of a triangle and
#computes the area using Heron's formula.
#(https://en.wikipedia.org/wiki/Heron%27s_formula)

import math

# side lengths of the triangle
side_a = float(input("Enter the length of side a: "))   #3
side_b = float(input("Enter the length of side b: "))   #4
side_c = float(input("Enter the length of side c: "))   #5
#                                                        =6
# the semi perimeter
semi_perimeter = (side_a + side_b + side_c) / 2

# area using Heron's formula
triangle_area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))

# result
print(f"The area of the triangle is: {triangle_area}")
