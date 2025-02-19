# Slicing and looping thru lists

# Slicing
shopping_list = ["potatoes","grapes","cuties","eggs","bread","mushrooms"]
#print(shopping_list[1:3]) #include start and end(non-inclusive)
#print(shopping_list[:3])  #only the end(non-inclusive)
#print(shopping_list[3:])  #only provide the start
#print(shopping_list[1:6:2]) #can also provide a step parameter

# Looping

# For --- in looping
#for element in shopping_list:
#    print(element)

# Using range() when you need indices
#for i in range(len(shopping_list)):  #0,1,2,3,4,5
#    print(i, shopping_list[i])

names = ["Pat", "Tempes", "Bishop"]
for name in names:
    print("Greetings, ", name, "!", sep="")
