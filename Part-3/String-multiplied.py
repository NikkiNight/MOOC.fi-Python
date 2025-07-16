"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added."
"""

# Write your solution here
word = str(input("Please enter a word: "))
amount = int(input("Please enter an amount: "))

print(word*amount)