"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 6

This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used.
The program should read the recipes from a file submitted by the user. Each recipe consists of three or more lines.
The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes,
and the remaining line or lines contain the ingredients used, one on each line.
The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file.

Part 1: Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments.
The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.

Part 2: Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments.
The function should go through the file and select all recipes whose preparation time is at most the number given.
The names of these recipes are again returned in a list, but the preparation time should be appended to each name.

Part 3: Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments.
The function should go through the file and select all recipes whose ingredients contain the given search string.
The names of these recipes are returned in a list just like in the second part, with the preparation time appended.
"""

# Write your solution here
# Part 1
def search_by_name(filename: str, word: str):
    recipes = {}

    with open(filename) as new_file:
        current_recipe = [] # List to store lines belonging to the same recipe

        for line in new_file:
            line = line.strip() # Removes newlines & spaces

            if line == "": # If line is blank, end of that recipe
                if current_recipe: # Safety check. Process if list is not empty
                    name = current_recipe[0]
                    time = int(current_recipe[1])
                    ingredients = current_recipe[2:]

                    recipes[name] = {"time": time, "ingredients": ingredients} # Add name, time & ingredients from current_recipe to recipes dictionary

                    current_recipe = [] # Delete current recipe, ready for the next one  

            else: # If the line isnt blank (still going throught the same recipe), store to current_recipe
                current_recipe.append(line)

        if current_recipe: # Process last recipe if file doesnt end with a blank line
            name = current_recipe[0]
            time = int(current_recipe[1])
            ingredients = current_recipe[2:]

            recipes[name] = {"time": time, "ingredients": ingredients}

    # Part 1. Search by name
    found_recipe = [] # List to store found recipes
    for recipe in recipes:
        if word in recipe.lower():
            found_recipe.append(recipe)
    
    return found_recipe

# Part 1 tests
#found_recipes = search_by_name("recipes1.txt", "cake")
#print(found_recipes)

# Part 2
def search_by_time(filename: str, prep_time: int):
    recipes = {}

    with open(filename) as new_file:
        current_recipe = [] # List to store lines belonging to the same recipe

        for line in new_file:
            line = line.strip() # Removes newlines & spaces

            if line == "": # If line is blank, end of that recipe
                if current_recipe: # Safety check. Process if list is not empty
                    name = current_recipe[0]
                    time = int(current_recipe[1])
                    ingredients = current_recipe[2:]

                    recipes[name] = {"time": time, "ingredients": ingredients} # Add name, time & ingredients from current_recipe to recipes dictionary

                    current_recipe = [] # Delete current recipe, ready for the next one  

            else: # If the line isnt blank (still going throught the same recipe), store to current_recipe
                current_recipe.append(line)

        if current_recipe: # Process last recipe if file doesnt end with a blank line
            name = current_recipe[0]
            time = int(current_recipe[1])
            ingredients = current_recipe[2:]

            recipes[name] = {"time": time, "ingredients": ingredients}

    # Part 2. Search by prep time
    found_recipe = [] # List to store found recipes
    for name, info in recipes.items():
        if info["time"] <= prep_time:
            found_recipe.append(f'{name}, preparation time {info["time"]} min')
    
    return found_recipe

# Part 2 tests
#found_recipes = search_by_time("recipes1.txt", 20)
#print(found_recipes)

# Part 3
def search_by_ingredient(filename: str, ingredient: str):
    recipes = {}

    with open(filename) as new_file:
        current_recipe = [] # List to store lines belonging to the same recipe

        for line in new_file:
            line = line.strip() # Removes newlines & spaces

            if line == "": # If line is blank, end of that recipe
                if current_recipe: # Safety check. Process if list is not empty
                    name = current_recipe[0]
                    time = int(current_recipe[1])
                    ingredients = current_recipe[2:]

                    recipes[name] = {"time": time, "ingredients": ingredients} # Add name, time & ingredients from current_recipe to recipes dictionary

                    current_recipe = [] # Delete current recipe, ready for the next one  

            else: # If the line isnt blank (still going throught the same recipe), store to current_recipe
                current_recipe.append(line)

        if current_recipe: # Process last recipe if file doesnt end with a blank line
            name = current_recipe[0]
            time = int(current_recipe[1])
            ingredients = current_recipe[2:]

            recipes[name] = {"time": time, "ingredients": ingredients}

    # Part 3. Search by ingredient
    found_recipe = [] # List to store found recipes
    for name, info in recipes.items():
        if ingredient in info["ingredients"]:
            found_recipe.append(f'{name}, preparation time {info["time"]} min')
    
    return found_recipe

# Part 3 tests
#found_recipes = search_by_ingredient("recipes1.txt", "eggs")
#print(found_recipes)