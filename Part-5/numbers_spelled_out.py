"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named dict_of_numbers(), which returns a new dictionary.
The dictionary should have the numbers from 0 to 99 as its keys.
The value attached to each key should be the number spelled out in words.
"""

# Write your solution here
def dict_of_numbers():
    dictionary = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",

        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",

        10: "ten",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    for num in range(100):
        if num in dictionary:
            continue
        else:
            tens = (num // 10) * 10 # Find the tens place (e.g. input 42, tens place is 40) using integer division
            ones = num % 10 # Find the ones place (e.g. input 42, ones place is 2) using modulo
            dictionary[num] = dictionary[tens] + "-" + dictionary[ones] # Combine the tens and ones (e.g. "forty" + "-" + "two")

    return dictionary        

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
