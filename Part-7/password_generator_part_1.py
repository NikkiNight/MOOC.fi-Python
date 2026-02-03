"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.
"""

# Write your solution here
import string
import random

def generate_password(length: int):
    password = "" # String to store password

    for i in range(length):
        letter = random.choice(string.ascii_lowercase) # Randomly choose a lowercase ASCII letter
        password += letter

    return password

# Tests
#print(generate_password(5))