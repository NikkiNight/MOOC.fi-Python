"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named invert(dictionary: dict), which takes a dictionary as its argument.
The dictionary should be inverted in place so that values become keys and keys become values.
"""

# Write your solution here
def invert(dictionary: dict):
    contents = list(dictionary.items()) # Store the dictionary items in a separate list

    dictionary.clear() # Clear the ORIGINAL dictionary

    for key, value in contents: # Loop through the stored dictionary items and assign the value as key and key as value
        dictionary[value] = key    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)