import turtle

leo = turtle.Turtle()
print(leo)

# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)
# leo.fd(100)
# leo.lt(90)

# def square(t):
#     """ Write a function that takes parameter t, which is a turle. It should use the turtle to draw a square.
#     """
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)

# square(leo)

# raphael = turtle.Turtle()
# square(raphael)

def square(t, length):
    """this function takes a parameter named t, which is a turtle, and another parameter length, which is a float. It should use the turtle to draw a swuare with side length, length"""

    for i in range(4):
        t.fd(length)
        t.lt(90)

        # generalization

square(leo, 150)

turtle.mainloop()

# when told pause, pause!!!