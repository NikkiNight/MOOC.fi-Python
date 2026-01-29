"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

The file lottery_numbers.csv containts winning lottery numbers in the following format:
Sample data
week 1;5,7,11,13,23,24,30
week 2;9,13,14,24,34,35,37
...etc...

Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.
The file has been corrupted. Lines in the file may contain the following kinds of errors:
- The week number is incorrect
- One or more numbers are not correct
- Too few numbers
- The numbers are too small or large
- The same number appears twice

Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.
"""

# Write your solution here
import re # Regex

def filter_incorrect():
    # Create the correct_numbers file
    with open("correct_numbers.csv", "w") as correct_file:
        pass

    # Reading the corrupt file
    with open("lottery_numbers.csv", "r") as corrupt_file:
        for line in corrupt_file:
            parts = line.split(";")

            header = parts[0]
            numbers = parts[1]

            # If header doesn't match "week " and a single-digit or double-digit number
            if not re.fullmatch(r"week \d+", header.strip()):
                continue

            # If there are more or less than 7 numbers
            number_count = numbers.split(",")
            if len(number_count) != 7:
                continue

            # If any numbers are negative
            if re.search(r"-\d+", numbers):
                continue

            # If numbers contains letters
            if re.search(r"[a-zA-Z]", numbers):
                continue

            # If any numbers are not between 0 and 39
            if any(int(num) < 1 or int(num) > 39 for num in number_count):
                    continue

            # If a number appears more than once
            if len(set(number_count)) != len(number_count): # "Set" counts all unique numbers, if less than 7 unique numbers are found, there are duplicates
                continue

            # Correct numbers are written to the file
            with open("correct_numbers.csv", "a") as correct_file:
                correct_file.write(line)

    return