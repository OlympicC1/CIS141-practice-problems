# Practice Problems with Booleans & If statements

# What do the following Boolean expressions evaluate to:
#print((5 > 3) and (2 == 2))
#True and True
#True

#(5 > 3) and (2 == 2)
#True   and True
#True
#print(("apple" == "pie") or (24 > 6))
#False              or True
#True

#print(not (-6 < 0))
#not True
#False

# not(-6 < 0)
'''
#Write an if-else that checks if a number supplied by the user is positive or not:
# Get input from user (num)
num = int(input("Please give me a number, any number: "))
# If num is greater(>) than zero(0) than state number is positive
if num > 0:
    print("You gave me a positive number!")
# Else, print a message statement the number is not positive
else:
    print("You gave me a number that's not positive.")

#Write a program that asks a person's age & Drivers License serving them alcohol
# Request person's age from user (age)
age =  int(input("Please give me your age: "))
# Request whether user has driver's license (dl)
dl = input("Do you have a driver's license? (Yes/No): ")
# If user is over 21 and a  drivers license, print that it's ok to serve them alcohol
if (age >= 21) and (dl == "Yes"):
    #if (age > 21) and (dl.lower() == "Yes".lower()): Makes case_insensitive
# Otherwise, print that they can't get alcohol
    print("It's ok to serve then alcohol:")
else:
    print("I can't permit you to buy alcohol without a valid drivers license and or because you are not over the age of 21!")


