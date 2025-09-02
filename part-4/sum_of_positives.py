"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named sum_of_positives, which takes a list of integers as its argument.
The function returns the sum of the positive values in the list.
"""

# Write your solution here
def sum_of_positives(my_list):
    result = 0
    for num in my_list:
        if num > 0:
            result += num

    return result

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)