"""
Author: Nicola "Nikki" Ward (@NikkiNight)
Project: MOOC.fi Python - Part 7

In this exercise you will write some functions which can be used in games that involve dice.

Instead of normal dice this exercise specifies non-transitive dice.

Please write a function named roll(die: str), which rolls the die specified by the argument.
Also write a function named play(die1: str, die2: str, times: int), which throws both dice as many times as specified by the third argument.
The function should return a tuple, the first item should be the number of times die 1 won, the second the number of times die 2 won,
and the third item should be the number of ties.
"""

# Write your solution here
import random

def roll(die: str):
    # Non-transitive dice declarations
    die_A = [3, 3, 3, 3, 3, 6]
    die_B = [2, 2, 2, 5, 5, 5]
    die_C = [1, 4, 4, 4, 4, 4]

    if die == "A":
        result = random.choice(die_A)

    elif die == "B":
        result = random.choice(die_B)

    else:
        result = random.choice(die_C)

    return result

def play(die1: str, die2: str, times: int):
    # Non-transitive dice declarations
    die_A = [3, 3, 3, 3, 3, 6]
    die_B = [2, 2, 2, 5, 5, 5]
    die_C = [1, 4, 4, 4, 4, 4]

    # Win counters
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for i in range(times):

        # Die 1 rolls
        if die1 == "A":
            die1_roll = random.choice(die_A)

        elif die1 == "B":
            die1_roll = random.choice(die_B)

        else:
            die1_roll = random.choice(die_C)

        # Die 2 rolls
        if die2 == "A":
            die2_roll = random.choice(die_A)

        elif die2 == "B":
            die2_roll = random.choice(die_B)

        else:
            die2_roll = random.choice(die_C)

        # Count wins
        if die1_roll > die2_roll:
            die1_wins += 1
        elif die1_roll < die2_roll:
            die2_wins += 1
        else:
            ties += 1

    return (die1_wins, die2_wins, ties)

# Tests roll function
#for i in range(20):
#    print(roll("A"), " ", end="")
#print()
#for i in range(20):
#    print(roll("B"), " ", end="")
#print()
#for i in range(20):
#    print(roll("C"), " ", end="")

# Tests play function
#result = play("A", "C", 1000)
#print(result)
#result = play("B", "B", 1000)
#print(result)