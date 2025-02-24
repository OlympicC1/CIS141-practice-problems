'''
#1. Write a funtion called count_vowels(input) that takes a string
    #and returns the number of vowels (a, e, i, o, u) in it.


# Function count_vowels that takes a parameter called input_string
def count_vowels(input_string):
# Create a variable to store the count of vowels to go to "0"
    vowel_count = 0
# Define a string with all vowels both lower and upper case
    vowels = "aeiouAEIOU"
# Loop through each character in the input_string
    for char in input_string: # Don't forget colons or spaces!!!
# Check if the character is in vowel string
        if char in vowels:
# If it is character is in the vowel string
            vowel_count += 1
# After loop return count of vowels
    return vowel_count
# My test run of functions and program
input_string = "Hello, Crystal, Have a great day!"
# Call my function
print(f"Number of vowels in '{input_string}':", count_vowels(input_string))



#2. Write a function called is_palindrome(s) that checks whether a string is a
    palidrome (reads the same forward and backward, ignoring case.)
    The function should return either True or False.
    Test: racecar (True), pikachu (False), Racecar (True)
    Input: string (s) # Use for practice problems
    Output: boolean
    Function body: lowecase s, flip s and save to new variable (filppled_s)
    and then compare s & flipped_s  #(now program, def)

#def is_palindrome(s):   #Now create body
    #print(s.lower())
#is_palindrome("Racecar")
def is_palindrone(s):   #Now create body
    lower_s = s.lower()
    #flipped_s = lower_s.reverse() Use this below from Python
    flipped_s = lower_s[::-1]
    #print(flipped_s)
    #print(s.lower())    #Testing
    return lower_s == flipped_s

print(is_palindromee("Racecar"))
print(is_palindrome("pikachu"))
print(is_palindrome("racecar"))
#is_palindrone("Racecar") To see the return we need to print
#is_palindrone("pikachu")

# Last step return a boolean





#3. In the game Pokemon, certain types of Pokemon do extra damage to other
    #types. For example, water is very effective to fight fire.
   #Write a function called type_advantage(attacker, defender) that takes
    #two Pokemon types as strings and returns "Super Effective", "Not Very Effective",
    #or "Neutral" based on simple type of effectivness rules. Your solution only needs
    #to work for these three sets of input:
    #print(type_advantage("Water", "Fire")) # "Super Effective"
    #print(type_advantage("Fire", "Water")) # "Not very Effective"
   # print(type_advantage("Electric", "Grass")) # "Neutral"
# Define the function called type_advantage that takes two parameters
def type_advantage(attacker, defender):
# Check if attacker is Water and defender is fire
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
# Now flip Water and Fire
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
# Check if the attacker is fire and defender is water
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
# Default case for any other combinations
    else:
        return "Neutral"
# Now example of working function...(wont lie got my fingers crossed.)
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
print(type_advantage("Fire", "Grass")) # "Neutral"




#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
#    based on age and whether the person has a vehice. Assume the following
#    rates:
#    * Adults (19-64): $10 without a vehicle, $20 with a vehicle


# Define the function called ferry_fare that had two parameters age & vehicle\
def ferry_fare(age, vehicle):
# Check if person is an adult between 19-64
    if age >= 19 and age <= 64:
# Check if the person has a vehicle
        if vehicle:
            return 20 # For adults with a vehicle
        else:
            return 10 # For adults without a vehicle
# Default if age does not fall into my specific category
    else:
            return 0 # for other age groups input invalid
print(ferry_fare(25, True))
print(ferry_fare(19, False))
print(ferry_fare(70, True))
print(ferry_fare(12, False))
