"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file.
The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.
Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc.
Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.
The final grade for the course is determined based on the sum of exam and exercise points.
"""

# wwite your solution here
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

            # Part 2
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

            # Part 2
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

        print(name, grade)    

students_dict = students(students_info)
students_dict = exercises(students_dict, exercise_data)
students_dict = exam_points(students_dict, exam_data)
print_info(students_dict, students_info, exercise_data, exam_data)  