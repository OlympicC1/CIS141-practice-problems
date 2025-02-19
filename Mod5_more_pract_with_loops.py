# More Practice Problems

# Problem 1: Write a while loop that sums from 1 to 50
counter = 1
#sum = 0
#while counter <= 50:
 #   sum += counter
  #  print("counter = ", counter, ": sum = ", sum)
   # counter += 1
#print(sum)

# Problem 2: Write a for loop that prints the even numbers from 1 to 20,
# but skip 10 using continue

#for i in range(1,21):   #1----20
#    if i is 10:
#       continue
#    if i % 2 == 0: #really awesome way to test if number is even
#       print(i)

# Problem 3: Write a program that creates a pyramd of asterisks to the console.
# For each row in the pyrmid, you use one loop to print the required number of spaces and another loop to
# print the required number of asterisks.
#      *      Row 1: 4 spaces, 1 stars
#     ***     Row 2: 3 spaces, 3 stars
#    *****    Row 3: 2 spaces, 5 stars
#   *******   Row 4: 1 space,  7 stars
#  *********  Row 5: 0 spaces, 9 stars

#for i in range(5): #0,1,2,3,4
#     # loop for creating spaces
#    for j in range(5 - 1 - i):
#         print(" ", end="")
#     # loop for creating asterisks
#    for k in range(1 + (2 * i)):
#        print("*", end="")
#     # print a new line
#    print("")

 # Making a new variable w/ row = any number you want
 # Using different variables also with j and k, can use underscore
row = 10
for i in range(row): #0,1,2,3,4
     # loop for creating spaces
    for _ in range(row - 1 - i):
         print("_", end="")   #"_" to add spaces
     # loop for creating asterisks
    for _ in range(1 + (2 * i)):
        print("*", end="")
     # print a new line
    print("")
