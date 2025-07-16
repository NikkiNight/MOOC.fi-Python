"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly."
"""

# Write your solution here
width = int(input("Please enter an width: "))
length = int(input("Please enter an length: "))

character = "#"
counter = 0

while counter != length:
    print(character * width)

    counter += 1