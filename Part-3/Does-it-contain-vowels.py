"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to input a string.
The program then prints out different messages if the string contains any of the vowels a, e or o.
You may assume the input will be in lowercase entirely."
"""

# Write your solution here
word = str(input("Enter a word: "))

if "a" in word:
    print("a found")
else:
    print("a not found")
if "e" in word:
    print("e found")
else:
    print("e not found")
if "o" in word:
    print("o found")
else:
    print("o not found") 