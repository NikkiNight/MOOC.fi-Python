"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named even_numbers, which takes a list of integers as an argument.
The function returns a new list containing the even numbers from the original list.
"""

# Write your solution here
def even_numbers(my_list):
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(num)

    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)