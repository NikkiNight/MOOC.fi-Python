"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a program which asks the user for words.
If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
"""

# Write your solution here
words = []  # Initialize an empty list

while True:
    word = input("Please enter a word: ")  # Prompt for input
    words.append(word)  # Add word to the list

    word_set = set(words)  # Create a set of unique words

    if words.count(word) >= 2:
        print(f"You typed in", len(word_set), "different words")
        break