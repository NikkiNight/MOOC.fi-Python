"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in a string.
The program then prints out all the substrings which end with the last character, from the shortest to the longest."
"""

# Write your solution here
word = str(input("Please enter a word: "))

length = len(word)

while length >= 0: 
    print(word[length:]) # Prints from last character to the first, one letter at a time
    length -= 1 # Loop counter. Also moves one letter closer to the beginning on each loop