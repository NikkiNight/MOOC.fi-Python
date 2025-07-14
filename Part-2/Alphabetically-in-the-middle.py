"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"Please write a program which asks the user for three letters.
The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
You may assume the letters will be either all uppercase, or all lowercase."
"""

# Write your solution here
letter1 = input("Please enter a letter: ")
letter2 = input("Please enter a second letter: ")
letter3 = input("Please enter a third letter: ")

letters = [letter1, letter2, letter3]

letters.sort() # Sort letters alphabetically

print(f"The letter in the middle is {letters[1]}")