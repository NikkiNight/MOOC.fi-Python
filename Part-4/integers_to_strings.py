"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named formatted, which takes a list of floating point numbers as its argument.
The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points.
The order of the items in the list should remain unchanged.
"""

# Write your solution here
def formatted(my_list):

    new_list = []

    for num in my_list:
        new_list.append(f"{num:.2f}")

    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)