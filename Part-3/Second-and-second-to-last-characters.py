"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for a string.
The program then prints out a message based on whether the second character and the second to last character are the same or not."
"""

# Write your solution here
word = str(input("Please enter a word: "))

index = len(word)

if word[1] == word[index - 2]:
    print("The second and the second to last characters are " + word[1])
else:
    print("The second and the second to last characters are different")