"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 1

"Please write a program which asks for the user's name.
If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost.
The price of a single portion is 5.90."
"""

# Write your solution here
name = input("Enter your name: ")

if name == "Jerry" or name == "jerry":
    print("Next please!")
else:
    portion = int(input("How many portions of soup? "))

    price = 5.90
    total = price * portion

    print(f"The total cost is {total}")
    print("Next please!")