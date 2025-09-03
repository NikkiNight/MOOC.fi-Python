"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named everything_reversed, which takes a list of strings as its argument.
The function returns a new list with all of the items on the original list reversed.
Also the order of items should be reversed on the new list. Also cannot modify the original list.
"""

# Write your solution here
def everything_reversed(my_list):
    new_list = []

    reverse_word_list = my_list.copy()  # Make a copy

    reverse_word_list.reverse() # Reverse list

    for word in reverse_word_list:
        new_list.append(word[::-1]) # Reverse words

    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

    my_list = ["here", "is", "a", "little", "longer", "list", "with", "more", "words"]
    new_list = everything_reversed(my_list)
    print(new_list)