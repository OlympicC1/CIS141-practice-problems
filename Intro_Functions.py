# FUNCTIONS
# Input goes in, output comes output

# Defining a function (): = Inputs, Parammeters and sometimes arguments.
# Anything with a colon will indet after enter

def greet(name): # Also known as side_effect
    #(name, para2, para3): #can add as many para as we need to complete
    print("Hello,", name) # Side effect now becasue of line 21 for me.
    # Changing the return value
    return "Hello, " + name
# Now were making the body of the program and still need to
# create/calling a function call_call
# For function name use ()

# greet("Lindsey")
# greet("Stephen")
# greet()

greeting = greet("Lindsey")
print(greeting)

# Return Values
def add (num1, num2):
    return num1+num2
    num1+num2  #Now were adding the function
    # Also will add lines 7,8
output = (add(7,8))
print(output)
# print(add(7,8))
