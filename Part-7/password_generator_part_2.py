"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

Please write an improved version of your password generator. The function now takes three arguments:
- If the second argument is True, the generated password should also contain one or more numbers.
- If the third argument is True, the generated password should also contain one or more of these special characters: !?=+-()#.

Despite these two additional arguments, the password should always contain at least one lowercase alphabet.
You may assume the function will only be called with combinations of arguments that are possible to formulate into passwords following these rules.
That is, the arguments will not specify e.g. a password of length 2 which contains both a number and a special characters,
for then there would not be space for the mandatory lowercase letter.
"""

# Write your solution here
import string
import random

def generate_strong_password(length: int, number: bool, special_char: bool):
    ALLOWED_SPECIAL_CHARS = "!?=+-()#" # Constant declaring acceptable special characters

    password = "" # String to store password  

    if number: # If number is True, add a number
        num = random.choice(string.digits)
        password += num
        
    if special_char: # If special_char is True, add a special character
        spec_char = random.choice(ALLOWED_SPECIAL_CHARS)
        password += spec_char

    letter = random.choice(string.ascii_lowercase) # Add at least one lowercase letter
    password += letter

    while len(password) < length: # If password is less than desired length
        letter = random.choice(string.ascii_lowercase) # Fill with lowercase ASCII letters
        password += letter

    return password

# Tests
#print(generate_strong_password(5, True, True))
#print(generate_strong_password(5, False, True))