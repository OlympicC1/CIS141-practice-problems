# Scope (Local vs. global)

# x = 10 # GlobalScope
# def my_function():
    #x = 5   # (localvariable)
    #y = 2   # (localvariable)
    #print("Inside function, x =", x)

# my_function()
# print("Inside function, x =", x)
# print("Inside function, y =", y)

# Pass by value (Immutable objects: int, float, str)
def modify(n):
    n = 10 # This creates a new local variable n
    print("Inside function", n) # 10

num = 5
# modify(num)
# print("Outside function:", num) # Still 5, becasue intergers are immutable

# Pass by Reference (mutable objects: list, dict)

def modify_list(lst):
    lst.append(4) # Modifies the original list

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers) # [1, 2, 3, 4] + The original list is changed

