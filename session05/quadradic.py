# ex04-06
# Define a function quadratic(a, b, c) to solve a quadratic equation and return the values of two roots:

import math
import time

def input_func():
    """Input function for quadratic()."""
    print('Let\'s solve for a quadratic function!')
    time.sleep(1.5)
    print('This function will retrieve roots for a quadratic function in a form of ax^2 + bx + c = 0.')
    time.sleep(3)
    print('Please enter real number for a, b, and c as instructed!')
    time.sleep(1.5)
    a = float(input('Enter a real number for a: '))
    b = float(input('Enter a real number for b: '))
    c = float(input('Enter a real number for c: '))
    print(quadratic(a, b, c))


def quadratic(a, b, c):
    """return two roots of a quadratic function"""

    if a == 0:
        return "This is not a quadradic function, but rather a linear function."
    else:
        pass

    inside_discriminant = b**2 - 4*a*c

    if inside_discriminant >= 0:
        discriminant = math.sqrt(inside_discriminant)
        quadradic_formula_positive = ((-b + discriminant)/(2*a))
        quadradic_formula_negative = ((-b - discriminant)/(2*a))

        if quadradic_formula_positive == quadradic_formula_negative:
            if quadradic_formula_positive % 1 == 0:
                quadradic_formula_positive = int(quadradic_formula_positive)
            else:
                pass
            answer = f'The 2 roots for the given quadradic equation are identical at {quadradic_formula_positive}.'
            return answer

        else:
            if quadradic_formula_positive % 1 == 0:
                if quadradic_formula_negative % 1 == 0:
                    quadradic_formula_positive = int(
                        quadradic_formula_positive)
                    quadradic_formula_negative = int(
                        quadradic_formula_negative)
                    answer = f'The 2 roots for the given quadradic equation are approximately {quadradic_formula_positive} and {quadradic_formula_negative}.'
                    return answer

            else:
                answer = f'The 2 roots for the given quadradic equation are approximately {quadradic_formula_positive:.2f} and {quadradic_formula_negative:.2f}.'
                return answer

    else:
        coefficient_imagenary = inside_discriminant/-1
        if coefficient_imagenary % 1 == 0:
            coefficient_imagenary = int(coefficient_imagenary)
        else:
            pass

        # discriminant = str(coefficient_imagenary) + 'i'
        if b % 2 == 0:
            a = a/2
            b = b/2
            coefficient_imagenary = coefficient_imagenary/2

        return f'The 2 roots for the given quadradic equation are ({b} + {coefficient_imagenary}i)/{2 * a} and ({b} 3- {coefficient_imagenary}i)/{2 * a}.'


input_func()

# print(math.sqrt(0))
# print(int(-1.00))

# Work on float and int conversion
