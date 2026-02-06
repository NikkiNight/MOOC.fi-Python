"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

In this exercise you will validate Finnish Personal Identity Codes (PIC).

Please write a function named is_it_valid(pic: str), which returns True or False based on whether the PIC given as an argument is valid or not.
Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the date of birth, X is the marker for century, yyy is the personal identifier and z is a control character.

The program should check the validity by these three criteria:
- The first half of the code is a valid, existing date in the format ddmmyy.
- The century marker is either + (1800s), - (1900s) or A (2000s).
- The control character is valid.

The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31,
and selecting the character at the index specified by the remainder from the string 0123456789ABCDEFHJKLMNPRSTUVWXY.
"""

# Write your solution here
from datetime import datetime

def is_it_valid(pic: str): # Finnish Personal Identity Codes (PIC) ddmmyyXyyyz

    # PIC length check
    if len(pic) != 11:
        return False

# ----

    # Splice date of birth, ddmmyy
    dob = pic[0:6]

    # Splice century marker, X
    century_marker = pic[6:7]

    # Splice personal identifier, yyy
    personal_identifier = pic[7:10]

    # Splice control character, z
    control_char = pic[10:11]

# ----

    day = dob[0:2]
    month = dob[2:4]
    year = dob[4:6]

    # Add correct prefix to year based on century marker, and evaluate century marker
    if century_marker == "+": # 1800's
        year = "18" + dob[4:6]
        valid_century_char = True
    elif century_marker == "-": # 1900's
        year = "19" + dob[4:6]
        valid_century_char = True
    elif century_marker == "A": # 2000's
        year = "20" + dob[4:6]
        valid_century_char = True
    else:
        return False

# ----

    # Evaluate format of date of birth
    try:
        int_day = int(day)
        int_month = int(month)
        int_year = int(year)

        check_dob = datetime(int_year, int_month, int_day)

        valid_dob = True

    except ValueError:
        return False

# ----

    # Evaluate the control character
    VALID_CHARS = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    nine_digits = int(pic[0:6] + pic[7:10]) # Gather dob (6 digits) and personal identifier (3 digits) together

    remainder_control_char = nine_digits % 31 # Divide the 9 digits by 31, stores the remainder

    # Compare remainder with valid characters
    if control_char == VALID_CHARS[remainder_control_char]: # Check the control character with the index of the valid characters
        valid_control_char = True
    else:
        valid_control_char = False

# ----

    # Final evaluation
    if valid_dob and valid_century_char and valid_control_char: # If all 3 are True
        return True
    else:
        return False

# Tests
#test = is_it_valid("230827-906F")
#test = is_it_valid("230827-906F1")