# Advanced String Concepts

# Strings Are Objects
text = "hello world"
#print(text.upper())       # This is upper case.
#print(text.capitalize())  # Capitalize only first letter
#print(text.lower())       # Lower case

# Immutabillty: Strings Cannot Change in Place(non-mutable)
# text[0] = "y"
new_text = "Y" + text[1:]
print(new_text)

# Comparison with Mutable Sequences(mute-able)
my_list = [1,2,3]
my_list[0] = "a"
print(my_list)

# .replace(), .split(), and .join()
phrase = "bananna"
new_phrase = phrase.replace("na", "NA")
print(new_phrase)
phrase2 = "Hello my name is Crystal"
new_phrase2 = phrase2.split(" ")
print(new_phrase2)
new_phrase3 = " ".join(new_phrase2)
print(new_phrase3)

# print() end & sep keyword args

print(text, phrase, phrase2)
print(text, phrase, phrase2, sep=": ")
print(text, phrase, phrase2, sep=": ", end="!!!!!")
print(text, phrase, phrase2, sep=": ", end="!!!!!\n")
print(text, phrase, phrase2, sep=": ", end="\n")
print(text, phrase, phrase2, sep=": ", end="%%%%&\n")



