"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1.
So, items 1 and 2 would be neighbours, and so would items 56 and 55.
Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.
"""

# Write your solution here
def longest_series_of_neighbours(my_list):
    if not my_list:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1

    return max_length

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))