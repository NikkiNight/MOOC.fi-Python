"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a new version of the program in the previous exercise.
In addition to the result it should also print out the calculation performed."
"""

# Write your solution here
limit = int(input("Enter a limit: "))

i = 0 # Base
num = 1

print("The consecutive sum: ", end="")

while i < limit:  
    print(f"{num} ", end="")

    i += num

    if i < limit:
        print("+ ", end="")
    num += 1    
print(f"= {i}")