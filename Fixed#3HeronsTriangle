# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

#Calculate the area of a trinagle using Heron's formula
#Run as Sideone = 3,Sidetwo = 4, Sidethree =5, total_area_vaule=6.0

def calculateTriangleArea(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) **0.5
    return area

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the thrid side: "))

area = calculateTriangleArea(side1, side2, side3)

sqrt_area = area ** 0.5

print("The area of your triangle is: " + str(area))
print("The square root of the area is: " + str(sqrt_area))



