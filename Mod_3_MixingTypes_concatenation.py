# Concatenation, Repetition, and Mixing Types
# can concatenate two string

# Concatenation (+)
strg1 = "Hello" + " " +"World" + "1"
#print(strg1)

# Concatentation with different types
score = str(500)
text = "Your score is "
#print(text + score)

# Repetition (*)
#print(strg1 * 3)
str2 = "####****0000"
#print(str2 * 10)

# In Keyword
strg3 = "apple"
#print("l" in strg3)
#print("o W" in strg1)
#print("word" in strg1)    ## T/F are called BOOLEANS

# Escape Sequence def: New line=\n, TAAB=\t, Single=\\, \"
str4 = "Bond,\n James Bond"
str5 = "Handley,\tLindsey" + "\nFoster, \tStephen" + "\nBecker, \tRichard" + "\nBlackwell,\tKevin"
#print(str4)
#print(str5)
str6 = "\\t is a escape character for a tab"
print(str6)
