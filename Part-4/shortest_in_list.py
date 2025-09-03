"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named shortest, which takes a list of strings as its argument.
The function returns whichever of the strings is the shortest. If more than one are equally short,
the function can return any of the shortest strings (there will be no such situation in the tests).
You may assume there will be no empty strings in the list.
"""

# Write your solution here
def shortest(my_list):

    shortest = "eleventh" # Predefined Initial value
    for word in my_list:
        if len(word) < len(shortest):
            shortest = word

    return shortest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)