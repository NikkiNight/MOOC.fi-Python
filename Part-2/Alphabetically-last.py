"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks the user for two words.
The program should then print out whichever of the two comes alphabetically last.
You can assume all words will be typed in lowercase entirely."
"""

# Write your solution here
word1 = input("Please enter a word: ")
word2 = input("Please enter a second word: ")

if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
elif word1 == word2:
    print("You gave the same word twice.")