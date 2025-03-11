

#2 Write a Python program that allows users to log their hiking trips. The program should:
#    - Use a while loop to repeatedly ask for a hike name and distance in miles
#    - Save each entry to hiking_log.txt (each hike on a new line)
#    - When the user presses 0, exit the loop & print the contents of hiking_log.txt


with open("hiking_log.txt", "a") as file:
    while True:
        hike_name = input("Enter hike name (or press 0 to exit): ")
        if hike_name == "0":
            break
        hike_distance = input("Enter hike distance in miles: ")
        file.write(f"{hike_name}: {hike_distance} miles\n")
with open("hiking_log.txt", "r") as file:
    contents = file.read()
    print("\nHiking Log:")
    print(contents)





