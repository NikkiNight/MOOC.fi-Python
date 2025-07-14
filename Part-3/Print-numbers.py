"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a program which prints out all the even numbers between two and thirty, using a loop.
Print each number on a separate line."
"""

# Write your solution here# Write your solution here
number = 2 # Even numbers
times = 1 # Times by value
answer = 0 # Initialize answer

while answer != 30:
    answer = number * times

    print(answer)

    times += 1 # Increment the times value