"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in."
"""

# Write your solution here
word = input("Enter a word: ")

length = len(word)

if length > 1:
    print(f"There are {length} in the word {word}")
print("Thank you!")