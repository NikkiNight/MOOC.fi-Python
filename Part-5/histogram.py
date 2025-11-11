"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named histogram, which takes a string as its argument.
The function should print out a histogram representing the number of times each letter occurs in the string.
Each occurrence of a letter should be represented by a star on the specific line for that letter.
"""

# Write your solution here
from collections import Counter

def histogram(word: str):
    character = "*"

    count = Counter(word)

    for letter in count:
        print(f'{letter}', (character * count[letter]))

if __name__ == "__main__":
    histogram("abba")