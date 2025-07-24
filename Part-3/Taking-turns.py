"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in a number.
The program then prints out the positive integers between 1 and the number itself,
alternating between the two ends of the range."
"""

# Write your solution here
num = int(input("Please enter a number: "))

i = 1
u = num

while i <= u:
    print(i) 
    if i != u: 
        print(u)
    i += 1
    u -= 1