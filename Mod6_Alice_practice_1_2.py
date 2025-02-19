# Problem 1
# You have a list of test scores.
# You want to calculate the average, identify the highest/lowest score,
# and see how many scores are above a certain threshold
# without using any additional libraries.
#scores = [80, 92, 78, 95, 85]
# Average(sum of all numbers) 1st step
#average = sum(scores) / len(scores)
#print("Average: ", average)

# Highest and lowest scores 2nd step (max/min)
#print("Max: ", max(scores))
#print("Min: ", min(scores))

# Count # over threshold of 90 3rd step
# Create a counter
#counter = 0
# loop through list of scores, if over 90 -> add to counter
#for score in scores:
#    if score > 90:
#        counter += 1
#print("# of Scores over 90: ", counter)


# Problem 2
# You have a list of names with possible duplicates,
# Remove duplicates while maintianing the original order.
names = ["Alice", "Jose", "Alice", "Charlie", "Jose", "Tanya"]

# Hint: in keyword from strings works with lists too:
#
#print("Alice" in names) #Value in the list?
#print("Sam" in names) #Substring is inlarger string?



# Start empty list to store unique names

#unique_names = []

# Loop through list of names check to see if name is already unique names if
# not in the list add to the list.
#for name in names:
#    if name in unique_names:
#        continue
#    else:
 #       unique_names.append(name)

#print(unique_names)

unique_names = []


for name in names:
    if name not in unique_names: # can make a single branch instead of two branches
        unique_names.append(name) # by getting rid of continue and else

print(unique_names)
