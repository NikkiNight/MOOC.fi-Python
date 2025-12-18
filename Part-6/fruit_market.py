"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents.
In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.
NB: the function does not take any arguments. The file you are working with is always named fruits.csv.
"""

# write your solution here
def read_fruits():
    fruits_dict = {} # Fruits dictionary

    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")

            fruit = parts[0]
            price = parts[1] # Str

            float_price = float(price) # Convert str to float

            fruits_dict[fruit] = float_price # Add fruit to dictionary as key, and float price as value

        return fruits_dict

if __name__ == "__main__":
    read_fruits()