"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2)."
"""

# Write your solution here
limit = int(input("Please enter a number: "))
base = int(input("Enter the base: "))

u = 0 # Counter

while base ** u <= limit:
    print(base ** u)
    u +=1