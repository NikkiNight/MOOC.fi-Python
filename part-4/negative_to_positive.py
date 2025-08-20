"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a program which asks the user for a positive integer N.
The program then prints out all numbers between -N and N inclusive, but leaves out the number 0.
Each number should be printed on a separate line.
"""

# Write your solution here
num = int(input("Please enter a positive number: "))

for i in range(-num, 0):
    print(i)

for x in range(1, num + 1):
    print(x)