from tkinter import N
import turtle
import math

leo = turtle.Turtle()
leo.speed(10)

# ex-01
# Modify the program to draw a square

# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)

# turtle.mainloop()
# turtle.bye()

leo.reset()

# ex-02.1


def square(t):
    """this function takes a parameter named t, which is a turtle. """

    for i in range(4):
        t.fd(100)
        t.lt(90)

        # generalization


# Test the function here
# square(leo)

leo.reset()

# ex-02.2


def square(t, length):
    """this function takes a parameter named t, which is a turtle, and another parameter length, which is a float. It should use the turtle to draw a swuare with side length, length"""

    for i in range(4):
        t.fd(length)
        t.lt(90)

        # generalization


# Test the function here
# square(leo, 150)

leo.reset()

# ex-02.3


def polygon(t, length, n):
    """this function takes a parameter named t, which is a turtle, and other parameters length and, which is a float. It should use the turtle to draw a swuare with side length, length. N represents the n-sided polygon."""

    for i in range(n):
        t.fd(length)
        t.lt(360/n)

        # generalization


# Test the function here
# polygon(leo, 10, 360)

leo.reset()

# ex-02.4


def circle(t, r):
    """this function takes a parameter named t, which is a turtle, and another parameter r, which is a radius of a circle. This function takes polygon() function to approximate a circle"""
    circumference = 2 * r * math.pi
    n = 360
    length = circumference/n
    polygon(t, length, n)

# circle(leo, 10)

leo.reset()

def arc(t, r, angle):
    """this function takes a parameter named, which is a turtle, and other parameters r and angle, which respectively are radius of a circle and fraction of circle to draw."""
    # Code credit to Professor Li for letting me use his code
    arc_length = 2 * r * math.pi * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# arc(leo, 100, 180)

leo.reset()

# ex-03.01

def square_circle(t, n, length, angle):
    """Repeat squares in a circle shape"""
    for i in range(n):
        square(t, length)
        t.lt(angle)

# square_circle(leo, 100, 5)

leo.reset()

#ex-03.02

def square_spiral(t, n, length, marginal_length, angle):
    """Repeat squares in a spiral shape"""
    leo.speed(10)
    for i in range(n):
        square(t, length)
        t.lt(angle)
        length = length + marginal_length

# square_spiral(leo, 60, 30, 4, 5)

def star(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(180 - angle)

# star(leo, 5, 30, 36)

leo.reset()

# ex-03.03

def star_spiral(t, n, length, marginal_length, angle, internal_angle):
    """Repeat stars in a spiral shape"""
    leo.speed(10)
    for i in range(n):
        star(t, 5, length, internal_angle)
        t.rt(angle)
        length = length + marginal_length

# star_spiral(leo, 60, 30, 4, 5, 36)

leo.reset()

# ex-03.04

def spiral(t, n, length, marginal_length, angle):
    """Spiral"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        length = length + marginal_length

spiral(leo, 60, 5, 1, 10)

turtle.mainloop()
