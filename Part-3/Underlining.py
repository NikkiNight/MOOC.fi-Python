"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for strings using a loop.
The program prints out each string underlined as shown in the examples below.
The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt."
"""

# Write your solution here
while True:
    word = str(input("Enter a word: "))

    if word != "":
        print(word)
        print("-" * len(word))
    else:
        break