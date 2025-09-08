"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument.
The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.
"""

# Write your solution here
def no_shouting(my_list):

    new_list = my_list.copy() # Copy list

    for word in my_list: # Cycle through the words in the original list
        if word.isupper(): # If word is upper
            new_list.remove(word) # Remove upper letter words from the new list

    return new_list # return the new list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)