"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.
Each row contains the information for a single student.
The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded,
and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.
"""

# write your solution here
students_info = input("Students file: ")
exercise_data = input("Exercise file: ")
exam_data = input("Exam file: ")

def students(students_info):
    # Read, add to dictionary, student id (key) + first name + last name (values)
    student_names = {}

    with open(students_info) as new_file:
        for line in new_file:
            parts = line.split(";")

            # ignore the header line
            if parts[0] == "id":
                continue

            # Remove excess whitespace \n
            parts[2] = parts[2].rstrip()

            # Part 2.
            student_id = parts[0]
            name = parts[1] + " " + parts[2]            

            # 
            student_names[student_id] = {
                "name": name,
                "exercises": 0,
                "exam": 0
            }

        return student_names

def exercises(student_names: dict, exercise_data):
    exercises_total = []

    with open(exercise_data) as new_file:
        for line in new_file:
            parts = line.split(";")

            # ignore the header line
            if parts[0] == "id":
                continue

            int_exercises = [int(item) for item in parts[1:]] # Convert exercises to int, skipping the id 

            # Part 2.
            student_id = parts[0]

            # Calc total exercises per row
            total = 0 # Variable to count total exercises
            for num in int_exercises:
                total += num

            # Append total to student based on id
            student_names[student_id]["exercises"] = total         

        return student_names

# Part 2 ----
def exam_points(student_names: dict, exam_data):
    exam_points_total = []

    with open(exam_data) as new_file:
        for line in new_file:
            parts = line.split(";")

            # ignore the header line
            if parts[0] == "id":
                continue

            int_exam_points = [int(item) for item in parts[1:]] # Convert exam points to int, skipping the id 

            # Part 2.
            student_id = parts[0]

            # Calc total exam points per row
            total = 0 # Variable to count total exercises
            for num in int_exam_points:
                total += num

            # Append total to student based on id
            student_names[student_id]["exam"] = total           

        return student_names

# ----

def print_info(student_names: dict, students_info, exercise_data, exam_data):
    # Prints Part 1 info (Name and exercises completed)
    #for student_id, (name, total) in student_names.items():
    #    print(name, total)  

    # Part 3 ----
    # Table variables
    col_name = "name"
    col_exercises = "exec_nbr"
    col_exercises_pts = "exec_pts."
    col_exam_pts = "exm_pts."
    col_total_pts = "tot_pts."
    col_grade = "grade"

    print(f'{col_name:30}{col_exercises:10}{col_exercises_pts:10}{col_exam_pts:10}{col_total_pts:10}{col_grade:10}') # Print column titles
    # ----

    # Prints Part 2 info (Name and exam points)
    for student_id, data in student_names.items():
        name = data["name"]
        exercises = data["exercises"]
        exam_points = data["exam"]

        exercise_points = exercises // 4
        total_points = exercise_points + exam_points
        
        grades = { # Dict to store grade ranges
            14: 0, # If the total is less than or equal to 14, grade is 0
            17: 1,
            20: 2,
            23: 3,
            27: 4,
            float("inf"): 5
        }

        for points, grade in grades.items():
            if total_points <= points:
                final_grade = grade
                break
                
        # Part 3
        print(f'{name:30}{exercises:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}') # Print table contents

students_dict = students(students_info)
students_dict = exercises(students_dict, exercise_data)
students_dict = exam_points(students_dict, exam_data) # ADDED
print_info(students_dict, students_info, exercise_data, exam_data) # ADDED EXAM_DATA     