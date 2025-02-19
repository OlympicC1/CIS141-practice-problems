# Lists: ordered collections of items (elements)
# my_list = [element1, element2, element3]

numbers = [1, 2, 3, 4, 5]
fruits = ["apple","banana","cherry"]
mixed = [1, "two", 3.0]
sublist = [[1,2,3],["one","two","three"],["I","II","III"]]

print(numbers)
print(sublist)
print(type(sublist))

# Empty Lists
empty = [] #tells python you want a list
print(empty)

# len() def of len is length
print(len(numbers))
print(len(empty))


# Indexing: starts at 0
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(["apple", "banana", "cherry"][2])
print(sublist[1])
print(sublist[1][2])
print(sublist[2][1])
