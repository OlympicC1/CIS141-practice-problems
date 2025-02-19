'''
#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
#n = int(input("Enter a positive integer: "))

# sum to zero
total_sum = 0

# counter to 1
i = 1

#while loop to sum all integers from 1 to user number
while i <= n:

    # value of i to total sum
    total_sum += i
    #Counter by 1
    i += 1

    # print final sum
print("The sum of integers from 1 to", n, "is:", total_sum)

#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.

 # string variable
my_string = "Olympic College"
 # use for loop to print character

for character in my_string:
    print(character.upper())

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

# for loop and range from 2 to 20

#2=start 21=range 2=skip
for number in range(2,21,2):
    print(number)


#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:

# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25

def print_multiplication_table():

    # loop numbers 1 to 5 for rows
    for i in range(1, 6):

        # loop numbers 1 to 5 for columns
        for j in range(1, 6):

        #the product with formatting
            print(f"{i * j:4}", end=" ")
        # new line after each row (print)
        print()

# call function display multiplication table
print_multiplication_table()


#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:

#Enter a number (0 to stop): 4
#You entered 4
#Enter a number (0 to stop): 7
#You entered 7
#Enter a number (0 to stop): 0
#Exiting...

while True:
    # user inputs a number
    number = int(input("Enter a number (0 to stop): "))

    # check if number is 0
    if number == 0:

        print("Exiting...")

        break #to leave loop
'''
    print(f"You entered {number}")

