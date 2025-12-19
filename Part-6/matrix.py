"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write two functions, named matrix_sum and matrix_max.
Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.
Please also write the function row_sums, which returns a list containing the sum of each row in the matrix.
"""

# write your solution here
def matrix_sum():
    total = 0 # Variable to store the addition of rows

    with open("matrix.txt") as new_file:
        for line in new_file:

            line = line.replace("\n", "")
            lines = line.split(",")

            int_lines = [int(item) for item in lines] # Convert str list to int list            

            for num in int_lines: # For each num in int_lines, 
                total += num # sum the values in the rows

        return total

def matrix_max():
    max_value = float("-inf") # Initialize to the smallest possible value, finding the max even if all values are negative

    with open("matrix.txt") as new_file:
        for line in new_file:

            line = line.replace("\n", "")
            lines = line.split(",")

            int_lines = [int(item) for item in lines] # Convert str list to int list 

            for num in int_lines: # For each num in int_lines,
                if num > max_value:
                    max_value = num

        return max_value

def row_sums():    
    rows_total = [] # Empty list to store row value addition results

    with open("matrix.txt") as new_file:
        for line in new_file:

            line = line.replace("\n", "")
            lines = line.split(",")

            int_lines = [int(item) for item in lines] # Convert str list to int list       

            total = 0
            for num in int_lines: # For each num in int_lines,
                total += num # sum the values in the rows

            rows_total.append(total) # Append to new list

        return rows_total