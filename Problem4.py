#4Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
#    Write a program that reads the poll.txt file
#    Count how many votes "yea" or "nay" received and print the results.


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
