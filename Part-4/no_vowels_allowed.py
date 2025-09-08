"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named no_vowels, which takes a string argument.
The function returns a new string, which should be the same as the original but with all vowels removed.
You can assume the string will contain only characters from the lowercase English alphabet a...z.
"""

# Write your solution here
import re

def no_vowels(my_string):

    new_string = re.sub('[aeiou]', "", my_string) # Remove all vowels with regex

    return new_string


if __name__ == "__main__":

    my_string = "this is an example"
    print(no_vowels(my_string))