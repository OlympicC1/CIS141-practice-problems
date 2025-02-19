'''
#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
# Create number list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sum of even numbers
sum_of_even_numbers = 0
# Repeat list of numbers for/if/sum
for number in numbers:
    # Check number even
    if number % 2 == 0:
        # Add even #'s to sum
        sum_of_even_numbers += number

print("The sum of all even numbers is:", sum_of_even_numbers)


#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
# List of defined strings
strings = ["Olympic", "Games", "are", "fun", "Olympic","events","are", "exciting", "Olympic"]
#Count Olympic
olympic_count = 0
# List of strings
for string in strings:
    # Check if string is Olympic
    if string == "Olympic":
        # Count
        olympic_count += 1
# Print result
print("The word 'Olympic' appears", olympic_count, "times in the list.")



#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.

# List of strings

strings = ["mouse", "rat", "hamster","roo", "mole", "pig", "cow", "kangaroo"]

# Filter list
filtered_list = []
#repeat list of strings with for/if using len(length) command
for string in strings:
    #length of the sting greater than 3 characters
    if len(string) > 3:
        # Add the string to list using append and filter
        filtered_list.append(string)

 # Print result
print("The filtered list of strings longer than three characters is:",filtered_list)


#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.

 # List of integers
numbers = [4, -1, 8, -5, 7, -2, -3, -8, -4, 1, -7, 2, 3, 5]

 # Count for positive and negative
positive_count = 0
negative_count = 0

  #List of numbers
for number in numbers:
    # Check positive
    if number > 0:
        positive_count += 1
        #Now count for negative
    elif number < 0:
            # Negative count
        negative_count += 1
# print both counts
print("The count of positive numbers is:", positive_count)
print("The count of negative numbers is:", negative_count)



#5. For a list of integers, use a loop to build a new list where each
#element is the square of the corresponding element
#corresponding element in the original list. Print the new list.

# List of integers
numbers = [1, 2, 3, 4, 5]
# List for storing squares
squared_numbers = []

for number in numbers:
    # square of the number
    square = number ** 2
    # Add to new list
    squared_numbers.append(square)
# Print result
print("The list of squared numbers is:", squared_numbers)
