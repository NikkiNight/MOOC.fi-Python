"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a program which asks the user to type in a string.
The program then prints each input character on a separate line.
After each character there should be a star (*) printed on its own line.
"""

# Write your solution here
word = input("Please enter a word: ")

for character in word:
    print(character)
    print("*")