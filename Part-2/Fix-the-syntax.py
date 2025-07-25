"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 2

"The following program contains several syntactic errors. 
lease fix the program so that the syntax is in order and the program works as specified by the examples below.

Please type in a number: 13
13 must be my lucky number!
Have a nice day!

Please type in a number: 101
The number was greater than one hundred
Now its value has decreased by one hundred
Its value is now 1
1 must be my lucky number!
Have a nice day!"

Original code:
# Fix the program
  number = input("Please type in a number: ")
  if number>100
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred)
      print("Its value is now"+ number)
 print(number + " must be my lucky number!")
 print("Have a nice day!)
"""
 
 # Fix the program
number = int(input("Please type in a number: "))

if number > 100:
    print("The number was greater than one hundred")

    number -= 100

    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")

print(f"{number} must be my lucky number!")
print("Have a nice day!")