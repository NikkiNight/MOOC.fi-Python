"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named longest(strings: list), which takes a list of strings as its argument.
The function finds and returns the longest string in the list.
You may assume there is always a single longest string in the list.
"""

# Write your solution here
def longest(strings: list):
    longest = max(strings, key=len)

    return longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))