# Accessing & Slicing Strings & Comparison

# Indexing, including out of range errors
str = "Olympic College Rangers"
length = len(str)

# Slicing & Stepping

#print(length)
#print(str[0]) # length
#print(str[1]) # length
#print(str[2]) # length

print(str[0:7]) # Slicing
print(str) # Slicing
#print(str[:7]) # Slicing
#print(str[16:])# Slicing

#print(str[::2]) #Stepping
#print(str[::3]) #Stepping
#print(str[::4]) #Stepping

# String Comparison ( == != < > < = >=)
#print("olympic"=="olympic") #True
#print("olympic"=="Olympic") #false(Upper-Case)
#print("olympic"!="olympic") #false(!)
print("olympic">"colllege") #True
print("Olympic">"colllege") #False(Upper_Case)

