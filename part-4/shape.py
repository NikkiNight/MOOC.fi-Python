"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 4

Please write a function named shape, which takes four arguments.
The first two parameters specify a triangle, as above, and the character used to draw it.
The first parameter also specifies the width of a rectangle, while the third parameter specifies its height.
The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.
The function should call the function line from the exercise above for the actual printing out.
Copy your solution to that exercise above the code for this exercise.
Please don't change anything in the line function.
"""

# Copy here code of line function from previous exercise and use it in your solution
def line(num, word):
    if word == "":
        print("*" * num)
    else:
        print(word[0] * num)

def shape(n, char, n2, char2):
    counter = 1
    counter2 = 1

    while counter <= n:        
        line(counter, char)
        counter += 1

    while counter2 <= n2:
        line(n, char2)
        counter2 += 1    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")