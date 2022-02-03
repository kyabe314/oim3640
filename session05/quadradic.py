# ex04-06
# Define a function quadratic(a, b, c) to solve a quadratic equation and return the values of two roots:

import math


def quadratic(a, b, c):
    """return two roots of a quadratic function"""
    inside_discriminant = b**2 - 4*a*c
    if inside_discriminant >= 0:
        pass
    else:
        return 'Discriment is an imagenary number.'
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
        answer = f'The 2 roots for the given quadradic equation are approximately {quadradic_formula_positive:.2f} and {quadradic_formula_negative:.2f}.'
        return answer

print(quadratic(1, 2, 1))

# print(math.sqrt(0))