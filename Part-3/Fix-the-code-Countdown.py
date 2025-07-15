"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please fix it so that it prints out the following:

Are you ready?
Please type in a number: 5
5
4
3
2
1
Now!"

Original code:

# Fix the program
print("Are you ready?")
number = int(input("Please type in a number: "))
while number = 0:
print(number)
print("Now!")
"""

# Fix the program
print("Are you ready?")
number = int(input("Please type in a number: "))

while number != 0:
    print(number)
    number -= 1 # Decrement number
print("Now!")