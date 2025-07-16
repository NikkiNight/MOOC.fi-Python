"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for a string.
The program then prints out the input string in reversed order, from end to beginning.
Each character should be on a separate line."
"""

# Write your solution here
word = str(input("Please enter a word: "))

index = len(word) # Counter

while index != 0:
    print(word[index - 1])
    index -= 1