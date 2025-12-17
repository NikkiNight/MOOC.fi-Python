"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different ways.
Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.
Please write a program which prints out a square of letters as specified in the examples below. You may assume there will be at most 26 layers.
"""

# Write your solution here
import string

alphabet = string.ascii_uppercase

layers = int(input("Layers: ")) # Asks user input for amount of layers

size = layers * 2 - 1 # Size of the square
center = size // 2

for row in range(size):
    for col in range(size):
        distance = max(abs(row - center), abs(col - center))
        letter = alphabet[distance]
        print(letter, end="")
    print()
