"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 3

"Please write a function named mean, which takes three integer arguments.
The function should print out the arithmetic mean of the three arguments."
"""

# Write your code here
def mean(num, num2, num3):    
    data = [num, num2, num3]
    result = sum(data) / len(data)
    print(result)

# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)