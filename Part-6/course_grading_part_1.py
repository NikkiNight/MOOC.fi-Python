"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

This program works with two CSV files. One of them contains information about some students on a course.
The other contains the number of exercises each student has completed each week.
Both CSV files also have a header row, which tells you what each column contains.

Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student.
"""

# write your solution here
students_info = input("Students file: ")
exercise_data = input("Exercise file: ")

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

            # ID (key) = first name & last name (value)
            student_names[parts[0]] = parts[1] + " " + parts[2] # Adds First name + space + Last name to ID key

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

            # Calc total exercises per row
            total = 0 # Variable to count total exercises
            for num in int_exercises:
                total += num

            # Append total to student based on id
            student_names[parts[0]] = (student_names[parts[0]], total)            

        return student_names

def print_info(student_names: dict, students_info, exercise_data):
    for student_id, (name, total) in student_names.items():
        print(name, total)        

students_dict = students(students_info)
students_dict = exercises(students_dict, exercise_data)
print_info(students_dict, students_info, exercise_data)        