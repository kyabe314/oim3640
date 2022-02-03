# ex 04-03~05




def my_abs1(number):
    """print the absolute value of the given number"""
    if number > 0:
        print(number)
    else:
        print(number * -1)

# my_abs(-100)
# my_abs(100)


def my_abs2(number):
    """return the absolute value for ex4-04"""
    if number > 0:
        return number
    else:
        return -number

# print(my_abs_2(-100))


def my_abs3(number):
    """return the absolute value for ex4-05"""
    classifier = isinstance(number, int | float)
    if classifier is True:
        if number > 0:
            return number
        else:
            return -number
    elif classifier is False:
        return "input neither integer nor float"


def input_func():
    """Input function for my_abs"""
    x = input('Choose function number from 1, 2, and 3 and enter here >>> ')
    if x == '1':
        my_abs1(float(input('Enter number for my_abs1 >>> ')))
    elif x == '2':
        my_abs2(float(input('Enter number for my_abs2 >>> ')))
    elif x == '3':
        my_abs3(float(input('Enter number for my_abs3 >>> ')))
    else:
        print('Invalid input. Please enter 1, 2, or 3.')
        input_func()

input_func()
