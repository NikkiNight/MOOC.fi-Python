"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which asks the user to type in a limit.
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user."
"""

# Write your solution here
limit = int(input("Enter a limit: "))

i = 0 # Base
num = 1

while i < limit: 
    i += num
    num += 1
print(i)