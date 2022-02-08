"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


def moon(weight_on_earth):
    """Convert the weight on earth to the weight on the moon 
    by multiplying the weight on earth by 0.165"""

    # pseudo-code
    # Create a function which converts the weight on earth to the weight on the moon
    # Multiply the weight on earth by 0.165, which is the proportional difference in gravity

    weight_on_earth = float(weight_on_earth)
    weight_on_moon = weight_on_earth * 0.165
    print(f'{weight_on_earth:.2f} kg of weight on earth is {weight_on_moon:.2f} kg of weight on the moon')


moon(input("Input a weight on earth in kg and I will convert it to weight on the moon in kg! >>> "))
