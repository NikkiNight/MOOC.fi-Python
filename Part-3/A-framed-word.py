"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre.
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.
If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations."
"""

# Write your solution here
word = str(input("Please enter a word: "))

WIDTH = 30
CHARACTER = "*"

sides = (28 - len(word)) // 2 # (28 characters remaining - word length) // 2 for both sides
extra = (28 - len(word)) % 2 # Odd number

space = " "

print(CHARACTER * WIDTH)
print(CHARACTER + " " * sides + word + " " * (sides + extra) + CHARACTER)
print(CHARACTER * WIDTH)