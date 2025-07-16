"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters.
If the strings are of equal length, the program should print out "The strings are equally long"."
"""

# Write your solution here
word1 = str(input("Please enter a word: "))
word2 = str(input("Please enter another word: "))

if len(word1) > len(word2):
    print(f"{word1} is longer")
elif len(word2) > len(word1):
    print(f"{word2} is longer")
else:
    print(f"The strings are equally long")