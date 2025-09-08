"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named most_common_character, which takes a string argument.
The function returns the character which has the most occurrences within the string.
If there are many characters with equally many occurrences, the one which appears first in the string should be returned.
"""

# Write your solution here
def most_common_character(first_string):

    char_list = list(first_string)

    most_common = ""
    for char in char_list:
        if char_list.count(char) > char_list.count(most_common):
            most_common = char

    return most_common

if __name__ == "__main__":

    first_string = "abcdbde"
    print(most_common_character(first_string))
