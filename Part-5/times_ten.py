"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary.
The keys of the dictionary should be the numbers between start_index and end_index inclusive.
The value mapped to each key should be the key times ten.
"""

# Write your solution here
def times_ten(start_index: int, end_index: int):
    dictionary = {}

    for i in range(start_index, end_index + 1):
        dictionary[i] = i * 10

    new_dictionary = {}

    for key in range(start_index, end_index + 1):
        new_dictionary.update({key: dictionary[key]})

    return new_dictionary

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)

    b = times_ten(1, 3)
    print(b)