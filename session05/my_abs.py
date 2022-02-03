def my_abs(number):
    """print the absolute value of the given number"""
    if number > 0:
        print(number)
    else:
        print(number * -1)

# my_abs(-100)
# my_abs(100)


def my_abs_2(number):
    """return the absolute value for ex4-04"""
    if number > 0:
        return number
    else:
        return -number

# print(my_abs_2(-100))


def my_abs_3(number):
    """return the absolute value for ex4-05"""
    classifier = isinstance(number, int | float)
    if classifier is True:
        if number > 0:
            return number
        else:
            return -number
    elif classifier is False:
        return "input neither integer nor float"


print(my_abs_3("1"))

# if number > 0:
#     return number
# elif number <= 0:
#     return -number
# elif number != int() or float():
#     return "invalid input"
