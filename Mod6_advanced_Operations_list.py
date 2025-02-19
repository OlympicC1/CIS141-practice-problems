# Advanced list Operations
numbers = [5, 2, 9, 1, 8, 4, 3, 2, 7, 3]
edibles = ["brocoli","apple","lettuce","cucumber", "tomato","raseberry","onion","dill","basil"]

# .sort() - changes list in place
#numbers.sort() #ascending order 1,2,3
#numbers.sort(reverse=True) #decending order 9, 8, 7
#print(numbers)

# .sorted() - leaves original list unchanged, returns new list

#sorted_numbers = sorted(numbers)
#print(numbers)
#print(sorted_numbers)
#edibles.sort()
#print(edibles)


# .reverse() - changes list in place
#numbers.reverse()
#print(numbers)
#edibles.reverse()
#print(edibles)

# .min(), .max(), .sum()
#print("Min: ", min(numbers))
#print("Max: ", max(numbers))
#print("Sum: ", sum(numbers))

# .index() - index searching
#tomato_index = edibles.index("tomato")
#print(tomato_index)
#cauliflower_index = edibles.index("cauliflower")
#print(cauliflower_index)
#cauliflower_index = edibles.index("cauliflower")
#print(cauliflower_index)
three_index = numbers.index(3)
print(three_index)
