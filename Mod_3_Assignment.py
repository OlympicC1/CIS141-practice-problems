
# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.

#Prompt user for a word   (Golden Nugget)
word = input("Enter a word: ")

#Prompt the user for the number of times to repeat the word (7)
times = int(input("How many times should it be repeated? "))
for _ in range(times):
    print(word) #Worked=7

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

#Prompt user for their name (Heather)
name = input("Enter your name: ")

#Prompt user for their age(23)
age = int(input("Enter your age: "))

#Calculate their age next year(24)
age_next_year = age + 1

#Print using string concatenation(worked)
print("Hello, " + name + "! You are " + str(age) + " years old. Next year, you will be " + str(age_next_year) + "years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)


#Prompt the user for a sentence
sentence = input("Enter a sentence: ")

#Prompt the user for a word to search for
word = input("Enter a word to search for: ")

#Check if the word is in the sentence
found = word in sentence

#(True or false)
print(found)     #true

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.

#prompt user a word (Goodnight)
word = input("Enter a word:")

#first index (2)
first_index = int(input("Enter first index: "))

#second index (5)
last_index = int(input("Enter last_index: "))

#slice word using user-defined indexes
sliced_word = word[first_index:last_index]

#print (odn)
print("Sliced word:", sliced_word)

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
print("sky", "stars", "moon", sep="|")
