"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named triangle, which draws a triangle of hashes, and takes one argument.
The triangle should be as tall and as wide as the value of the argument.
The function should call the function line from the exercise above for the actual printing out.
Copy your solution to that exercise above the code for this exercise.
Please don't change anything in the line function.
"""

# Copy here code of line function from previous exercise
def line(num, word):
    if word == "":
        print("*" * num)
    else:
        print(word[0] * num)

def triangle(size):
    # You should call function line here with proper parameters
    counter = 1
    while counter <= size:
        line(counter, "#")
        counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
