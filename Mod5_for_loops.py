# For loops

#string = "Hello"
#for item in some_sequence:
#for char in string:
    #print(char,"!")
    #can add to char
    #print(char)
#print("Exited for loop")
    # can also shorten "item" for "i"
    # do something with item

# range(stop) -> range(5) -> 0,1,2,3,4
# range(start,stop) -> range(2,6) -> 2,3,4,5
# range(start, stop, step) -> range(2,10) (This is "step")-> 2,4,6,8
#                           -> range(3,10,3) -> 3,6,9("step example")
# three different ways to use range in a seq.

#for i in range(5): # = 0,1,2,3,4 "Range"
#    print(i)
#print("End of loop")

#range(stop)
#range(start, stop, step)

#range (0,101,2)
#for i in range(0,101,2):
#    print(i)
#print("End of loop")

# Try to loop through the string "Programming" and print ever 3rd letter

#string = "Programming"  #0, 3, 6, 9
#for i in range(0,len(string),3):     # Reminder len="length of string"
    #print(string[i])                       # 3=the step

#for item in range(3,6,9):
    #print(string, sep='range')
#print("Exited for loop")
