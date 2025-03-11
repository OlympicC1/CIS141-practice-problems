#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
#    - Reads the file
#    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
#    - Counts how many times each word appears
#    - Creates a dictionary of the words and their counts
#    - Print the dictionary to the console


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
