"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a function named largest, which reads the file and returns the largest number in the file.
Notice that the function does not take any arguments.
The file you are working with is always named numbers.txt.
"""

# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for line in new_file:
            for line_str in line.strip().split(): # Convert str to int
                num = int(line_str)

                if num > largest:
                    largest = num

    print(largest)
    return largest

if __name__ == "__main__":
    largest()