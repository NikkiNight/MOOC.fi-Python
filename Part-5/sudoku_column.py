"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Please write a function named column_correct(sudoku: list, column_no: int), which takes a two-dimensional array representing a sudoku grid,
and an integer referring to a single column, as its arguments. Columns are indexed from 0.
The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.
"""

# Write your solution here
def column_correct(sudoku: list, column_no: int):
    seen = []
    check_column = [] # Building the column

    for row in sudoku: # Takes each digit based on column_no and adds it to check_column
        num = row[column_no]
        check_column.append(num)

    for num in check_column:
        if num == 0:
            continue
        if num in seen:
            return False
        else:
            seen.append(num)
    return True

if __name__ == "__main__":

    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
