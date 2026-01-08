"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

The file solutions.csv contains some solutions to mathematics problems, on each line the format is name_of_student;problem;result.
All the operations are either addition or subtraction, and each has exactly two operands.

Please write a function named filter_solutions() which:
Reads the contents of the file solutions.csv
writes those lines which have a correct result into the file correct.csv
writes those lines which have an incorrect result into the file incorrect.csv

Please write the lines in the same order as they appear in the original file. Do not change the original file.
"""

# Write your solution here
def filter_solutions():
    students = {}
    i = 1 # counter as unique key for each student's entry

    open("correct.csv", "w").close() # Clear contents of files for tests
    open("incorrect.csv", "w").close() # Clear contents of files for tests

    with open("solutions.csv", "r") as my_file:
        for line in my_file:
            parts = line.split(";")

            # Remove excess white space & \n
            parts[2] = parts[2].rstrip()

            # Variables for dictionary
            name = parts[0]
            problem = parts[1]
            result = parts[2]

            # Assign dictionary info to variables
            students[i] = { # i counter
                "name": name,
                "problem": problem,
                "result": result
            }

            # Increase i counter for next student
            i += 1

        for data in students.values():
            student_name = data["name"]
            equation = data["problem"]
            answer = int(data["result"])

            equation_result = eval(equation) # Evaluate the equation (Don't use on untrusted user inputs due to code injection)

            print(equation_result)
            print(f'answer {answer}')

            if equation_result == answer:
                # Append data to correct.csv file
                with open("correct.csv", "a") as correct_file:
                    correct_file.write(f'{student_name};{equation};{answer}\n')
            else:                
                # Append data to incorrect.csv file
                with open("incorrect.csv", "a") as incorrect_file:
                    incorrect_file.write(f'{student_name};{equation};{answer}\n')

# Tests    
#data = filter_solutions()
#print(data)