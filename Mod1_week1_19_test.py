# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air.")
print("Long ago, the four nations lived together in harmony.")
print("Then, everything changed when the Fire Nation attacked.")



# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
x =5
y = 16
x = y * 115
print(x,y)



# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
#Calculate the area of a trinagle using Heron's formula
#Run as Sideone = 3,Sidetwo = 4, Sidethree =5, total_area_vaule=6.0

def calculateTriangleArea(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

side1 = float(input("Enter the length of the first side:"))
side2 = float(input("Enter the length of the second side:"))
side3 = float(input("Enter the length of the thrid side:"))

area = calculateTriangleArea(side1, side2, side3)

print("The area of your triangle is: " + str(area))



# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

import math

def compute_statistics(numbers):

    if len(numbers) != 5:
     return "Please provide exactly five numbers."

    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    range_ = maximum - minimum

    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)

    return {
     "Total": total,
     "Average": average,
     "Minimum": minimum,
     "Maximum": maximum,
     "Range": range_,
     "Standard Deviation": std_deviation
