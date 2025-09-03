"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named length_of_longest, which takes a list of strings as its argument.
The function returns the length of the longest string.
"""

# Write your solution here
def length_of_longest(my_list):

    longer = ""
    for word in my_list:
        if len(word) > len(longer):
            longer = word

    return len(longer)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)