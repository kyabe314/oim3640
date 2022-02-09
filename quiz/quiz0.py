"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


def moon():
    """Convert the weight on earth to the weight on the moon 
    by multiplying the weight on earth by 0.165"""

    # pseudo-code
    # Create a function which converts the weight on earth to the weight on the moon
    # Multiply the weight on earth by 0.165, which is the proportional difference in gravity
    weight_on_earth = input(
        "Input a weight on earth in kg and I will convert it to weight on the moon in kg! >>> ")
    weight_on_earth = float(weight_on_earth)
    weight_on_moon = weight_on_earth * 0.165
    print(f'{weight_on_earth:.2f} kg of weight on earth is {weight_on_moon:.2f} kg of weight on the moon.')

# Commented out for the testing of question 2
# moon()


"""
Question 2:
Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.
Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Jupiter = weight on Earth * 2.528
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


def planet(weight_on_earth, name):
    """take weight on earth as the first arguement. Convert the weight on earth to weight on a planet specified in the second arguement."""

    # pseudo-code
    # 1. Take the disignated 2 parameters when calling the function
    # 2. Write a conditional statement that leads to a different conversion path depending on the input of the planet
    # 3. return the value

    weight_on_earth = float(weight_on_earth)

    if name == 'Moon':
        weight_on_moon = weight_on_earth * 0.165
        return weight_on_moon
    elif name == 'Mars':
        weight_on_mars = weight_on_earth * 0.378
        return weight_on_mars
    elif name == 'Jupiter':
        weight_on_jupiter = weight_on_earth * 2.528
        return weight_on_jupiter


print(planet(80, 'Jupiter'))
