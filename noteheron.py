'''
# Area of triangle by Herons Formula
import math
a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))
$p = (a + b + c) / 2$
$$s = sqrt{p(p-a)(p-b)(p-c)},$$
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area =",area)
'''# Write your code here :-)
