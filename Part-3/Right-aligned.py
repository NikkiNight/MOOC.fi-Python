"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed.
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
You may assume the input string is at most 20 characters long."
"""

# Write your solution here
word = str(input("Please enter a word: "))

length = len(word)
character = "*"

while length < 20 - 1:
    character += "*"
    length += 1

print(character + word) 