# Write function(s) to repeat a simulation 10 times. In each simulation, roll 100 dices and print the sum

# Pseudo-code
# The first function will roll the dice and print the result, random-in (1, 6)
# The second code will repeat the first function for a given number of times (10 in this case)

# function 1 - roll 100 dice, and print the sum
# 1. create a variable to store the sum of repetition, initialized at 0
# 2, import random library to 
# 3. repeat the following step(s) 100 times
#   - get a random integer in range(1, 6)
#   - add the random integer to result
# 4. print the result

import random

# underscore for not-indexing

def simulation(num_dice=100):
    """roll 100 dice ad print the sum"""
    result = 0
    for _ in range(num_dice):
        result += random.randint(1, 6)
    print(result, result/num_dice)

# simulation() # expected value


# function 2 - repeat the simulation 10 times
# 1. repeat the following step(s) 10 times
#   - function 1

def repeat_simulation(n):
    """repeat simulation n times"""
    for i in range(n):
        simulation(1000)

repeat_simulation(10)