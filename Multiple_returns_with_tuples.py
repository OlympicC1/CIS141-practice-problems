# By default functions return nothing

def print_message():
    print("This function doesn't return a value.")
#result = print_message()
#print(result)  # None

# Use return keyword to return something

adivsor1, advisor2 = "", ""

def cis_faculty_advisor(discipline):
    if discipline == "programming":
        return "Lindsey Handley", "Stephen Foster" # [immutable]brakets are what seperates
        # them from a list, [tuple is a lot like a list] again with brackets][[]] not ()
    elif discipline == "security":
        return "Kevin Blakcwell"
    elif discipline == "web":
        return "Peter Bill"
    else:
        return "Richard Becker"
result = cis_faculty_advisor("security")
#result = cis_faculty_advisor("programming")
#adivsor1, advisor2 = cis_faculty_advisor("programming")

# result = cis_faculty_advisor("programming")
result = cis_faculty_advisor("security")
if(type(result) == tuple): #
    adivsor1, advisor2 = result
else:
    adivsor1 = result
    advisor2 = result
result = cis_faculty_advisor("programming")
if(type(result) == "tuple"): # With "('Lindsey Handley', 'Stephen Foster')
# ('Lindsey Handley', 'Stephen Foster')"
#if(type(result) == tuple): # WITHOUT Lindsey Handley
#Stephen Foster
    adivsor1, advisor2 = result
else:
    adivsor1 = result
# advisor2 = result
print(adivsor1)
print(advisor2)

#print(type(result))
#if(result) == ):
#adivsor1, advisor2
#print(result)
#print(adivsor1)
#print(advisor2)

# adivsor1, advisor2 = cis_faculty_advisor("programming")
# A special way to save tuples\ unpack them in one variable

# Returning multiple values


