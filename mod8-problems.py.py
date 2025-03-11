'''

#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.

with open("gardening_tips.txt", "r") as file:
    tips = file.readlines()


    for tip in tips:
        print(tip.strip())

'''


#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt


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


'''

#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console

def count_word_frequency():
    with open('song_lyrics.txt', 'r') as file:
        lyrics = file.read().lower()

    words_to_count = []
    for i in range(5):
        word = input(f"Enter word {i+1} to count: ").lower()
        words_to_count.append(word)

    word_count = {word: 0 for word in words_to_count}

    lyrics_words = lyrics.split()

    for word in lyrics_words:
        if word in word_count:
            word_count[word] += 1
    print("\nWord Frequency Dictionary:")
    print(word_count)

if __name__ == "__main__":
    count_word_frequency()


'''


#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.

def count_votes():
    with open('poll.txt', 'r') as file:
        votes = file.read().strip().split(',')

    yea_count = 0
    nay_count = 0

    for vote in votes:
        if vote.strip().lower() == 'yea':
            yea_count += 1
        elif vote.strip().lower() == 'nay':
            nay_count += 1

    print(f"Yea votes: {yea_count}")
    print(f"Nay votes: {nay_count}")

if __name__ == "__main__":
    count_votes()

'''
