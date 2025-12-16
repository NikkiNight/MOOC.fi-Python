"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 5

Part 1: adding students
First write a function named add_student, which adds a new student to the database.
Also write a preliminary version of the function print_student, which prints out the information of a single student.

Part 2: adding completed courses
Please write a function named add_course, which adds a completed course to the information of a specific student in the database.
The course data is a tuple consisting of the name of the course and the grade.

Part 3: repeating courses
Courses with grade 0 should be ignored when adding course information.
Additionally, if the course is already in the database in that specific student's information,
the grade recorded in the database should never be lowered if the course is repeated.

Part 4: summary of database
Please write a function named summary, which prints out a summary based on all the information stored in the database.
"""

# Write your solution here
def add_student(students: list, name: str):
    students[name] = [] # Adds students to the database

def print_student(students: list, name: str):
    if name in students: # If the students name exists in the dictionary

        if len(students[name]) == 0: # If there are no completed courses
            print(f'{name}:')
            print(" no completed courses")
        else:
            print(f'{name}:')                    
            total_courses = len(students[name]) # Prints amount of courses
            print(f' {total_courses} completed courses:')

            for (course_name, grade) in students[name]: # Prints courses
                print(f"  {course_name} {grade}")

            # Calc the average grade
            total_grades = 0
            for (course_name, grade) in students[name]: # For the course_name and grade in students name
                total_grades += grade # Sum the grades
                average = total_grades / len(students[name]) # Sum divided by amount of courses
            print(f' average grade {average}')
    else: # If the students name doesnt exist in the dictionary
        print(f'{name}: no such person in the database')

def add_course(students: list, name: str, course_tuple: tuple):
    course, grade = course_tuple # Assigns course_tuple seperately to course and grade respectively

    for existing_course, existing_grade in students[name]: # For existing course and existing grade under students name
        if existing_course == course: # If the course exists
            if existing_grade >= grade: # If the existing grade is better than or equal to the new grade
                return # Exit
            else: # If the existing grade is less than the new grade
                students[name].remove((existing_course, existing_grade)) # Remove the old course and grade
                break # Go to next condition

    if grade > 0: # If the grade is greater than 0
        students[name].append((course, grade))

def summary(students: list):
    print(f'students {len(students)}') # Prints amount of students in the dict

    # Calc the student with the most courses
    most_courses = max(students, key=lambda name: len(students[name])) # In Students, based on name, find the student with the most courses taken
    count = len(students[most_courses]) # Count the amount of courses taken by that student

    print(f'most courses completed {count} {most_courses}') # Prints amount of courses taken and then the student name

    # Calc the best average grade
    best_average = 0 # Store the best grade average
    best_student = "" # Store the best grade average students name

    for student in students: # For student (name) in students dictionary
        grades = [] # Empty list to store grades

        for course, grade in students[student]:
            grades.append(grade)

        average = sum(grades) / len(grades)

        # Updating the best grade average and students name
        if average > best_average:
            best_average = average
            best_student = student

    print(f'best average grade {best_average} {best_student}')

if __name__ == "__main__":
    students = {}

    #add_student(students, "Peter")
    #add_student(students, "Eliza")

    #print_student(students, "Peter")
    #print_student(students, "Eliza")
    #print_student(students, "Jack")

    #add_course(students, "Peter", ("Introduction to Programming", 3))
    #add_course(students, "Peter", ("Advanced Course in Programming", 2))

    #print_student(students, "Peter")

    #add_student(students, "Peter")
    #add_student(students, "Emily")
    #print_student(students, "Peter")
    #print_student(students, "Emily")
    #print_student(students, "Andy")

    #add_student(students, "Peter")
    #add_course(students, "Peter", ("Introduction to Programming", 5))
    #print_student(students, "Peter")

    #add_student(students, "Peter")
    #add_course(students, "Peter", ("Software Development Methods", 0))
    #print_student(students, "Peter")

    #add_student(students, "Peter")
    #add_course(students, "Peter", ("Software Development Methods", 5))
    #add_course(students, "Peter", ("Software Development Methods", 1))
    #print_student(students, "Peter")

    #add_student(students, "Peter")
    #add_student(students, "Eliza")
    #add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    #add_course(students, "Peter", ("Introduction to Programming", 1))
    #add_course(students, "Peter", ("Advanced Course in Programming", 1))
    #add_course(students, "Eliza", ("Introduction to Programming", 5))
    #add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    #summary(students)