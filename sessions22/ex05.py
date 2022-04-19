class Rubiks_cube:
    """Represents attributes of a Rubik's cube"""

    def __init__(self, sides = 6, color = 6, length = 3, width = 3, height = 3):
        self.null = list()
        self.sides = sides
        self.color = color
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        return (
            f'The rubik\'s cube has {self.sides} sides, {self.color} colors.'
            f'In addtion, the size of the rubik\'s cube is as follows:'
            f'Length is {self.length} cm, width is {self.width}, and height is {self.height} cm.'
        )
    
    def __subtract__(self, other):
        colors = self.color - other
        return colors
    
    def __add__(self, other):
        colors = self.color + other
        return colors
