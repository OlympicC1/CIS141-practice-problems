#1. Construct a truth table for the expression:
#(A AND B) OR (NOT B) where A and B each can be True or False.
#Your truth table should be commented out (as it's not valid Python code!)
# I used the table from our lecture lessons.

# A B   (A OR B)    (A AND B)   NOT(A AND B)    (A OR B) AND NOT (A AND B)
# T T   T            T              F            F
# T F   T            F              T            T
# F T   T            F              T            T
# F F   F            F              T            F


print("A   | B   | A AND B | NOT B | (A AND B) OR (NOT B)")
print("---------------------------------------------------")

# through A and B values
for A in [True, False]:
    for B in [True, False]:
        # values direct
        and_result = A and B
        not_b = not B
        final_result = and_result or not_b

        # 'T' or 'F'
        A_value = "T" if A else "F"
        B_value = "T" if B else "F"
        and_value = "T" if and_result else "F"
        not_b_value = "T" if not_b else "F"
        final_value = "T" if final_result else "F"

        # I used our concatenation lesson and pipes for creating my True or False Table.
        print(A_value + "   | " + B_value + "   | " + and_value + "       | " + not_b_value + "     | " + final_value)


#2. The headlights of a car should only automatically turn on when the
#daylight outside is below a certain threshold. If a sensor threshold
#is below the number 8,print "Headlights On"; otherwise, print "Headlights Off".

# Get daylight sensor value
sensor_value = int(input("Enter the daylight sensor value (0-10): "))

#Now check sensor_value for Headlights On or Headlights Off.
if sensor_value < 8:
    print("Headlights On")
else:
    print("Headlights Off")


#3. Prompt the user for their bank balance.
#Evaluate whether the balance is less than $100.
#Print True if the user’s balance is below $100; print False, otherwise.

#Prompt user for bank balance
balance = float(input("Enter your bank balance please: "))
#If the balance is less than $100
print(balance < 100)

#4. A theater wants to enforce age restrictions for movie tickets.
#Ask the user for their age, and tell them whether they can see
#G (appropriate for under 13), PG-13 (appropriate for 13 to 17),
#or R (appropriate for over 18) rated movies.

#Ask user for age
age = int(input("How old are you? "))

#Now see which Movies they are allowed to watch

if age < 13:
    print("You can watch G-rated movies.")
elif age >= 13 and age < 18:
    print("You can watch G and PG-13 movies. ")
else:
    print("You can watch G, PG-13, and Rated-R movies. ")


#5. A store charges $5 for shipping on any order under $50.
#If the order amount is $50 or more, shipping is free.
#Ask the user for the order total and print the total cost, including shipping.

#Ask User for their total Order

order_total = float(input("Enter your order total please: "))

#Now see if shipping is required

if order_total < 50:
    total_cost = order_total +5 #This should make program charge $5 for shipping
else:
    total_cost = order_total #This should make the program Free shipping because order is over $50

#Final cost

print("Total cost including shipping: $", total_cost)
