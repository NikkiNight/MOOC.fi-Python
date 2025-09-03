"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named list_sum which takes two lists of integers as arguments.
The function returns a new list which contains the sums of the items at each index in the two original lists.
You may assume both lists have the same number of items.
"""

# Write your solution here
def list_sum(a, b):
    list_sum = []
    for i in range(len(a)):
        list_sum.append(a[i] + b[i])

    return list_sum

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]