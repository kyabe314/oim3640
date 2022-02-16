from tabulate import tabulate
import math

# ex-01.1


def one_to_ten():
    """
    This function sums up integers from 1 to 10, and return the sum.
    """
    sum_1_to_10 = 0

    for i in range(1, 11):
        sum_1_to_10 += i

    return sum_1_to_10

# test code
# print(one_to_ten())

# ex-01.02


def one_to_thousand():
    """
    This function sums up integers from 1 to 1000, and return the sum.
    """
    sum_1_to_1000 = 0

    for i in range(1, 1001):
        sum_1_to_1000 += i

    return sum_1_to_1000

# test code
# print(one_to_thousand())

# ex-01.03


def one_to_thousand_odd():
    """
    This function sums odd integers from 1 to 1000, and returns the sum.
    """
    sum_1_to_1000_odd = 0

    for i in range(1, 1001):
        if i % 2 == 1:
            sum_1_to_1000_odd += i

    return sum_1_to_1000_odd

# test code
# print(one_to_thousand_odd())

# ex-02.01

# 1. What is the value of the variable count that is printed out (at the print statement) on iteration 0?
# 2. What is the value of the variable count that is printed out (at the print statement) on iteration 1?
# 3. What is the value of the variable count that is printed out (at the print statement) on iteration 2?
# 4. What is the value of the variable count that is printed out (at the print statement) on iteration 3?
# 5. What is the value of the variable count that is printed out (at the print statement) on iteration 4?

# 1. 12
# 2. 24
# 3. 36
# 4. 48
# 5. 60

# 1. What is the value of the variable count that is printed out (at the print statement) on iteration 0?
# 2. What is the value of the variable count that is printed out (at the print statement) on iteration 1?
# 3. What is the value of the variable count that is printed out (at the print statement) on iteration 2?
# 4. What is the value of the variable count that is printed out (at the print statement) on iteration 3?
# 5. What is the value of the variable count that is printed out (at the print statement) on iteration 4?

# 1. 12
# 2. 12
# 3. 12
# 4. 12
# 5. 12

# 1. How many times will the print statement be executed?
# 2. What is the largest value of the variable iteration that will be printed out (at the print statement)?
# 3. What is the largest value of the variable count that will be printed out (at the print statement)?
# 4. What is the smallest value of the variable count that will be printed out (at the print statement)?

# 1. Never
# 2. None
# 3. None
# 4. None

# testing the third loop of ex-02.01


def ex_02_01_03():
    """
    Checking for 'iteration' and 'count' using loops.
    """
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
            if iteration % 2 == 0:
                break
    print("Iteration " + str(iteration) + "; count is " + str(count))
    iteration += 1

# test code
# ex_02_01_03()


# ex-02.02

def one_to_ten_while():
    """
    This function sums up integers from 1 to 10 using 'while' loop, and returns the sum.
    """
    sum_1_to_10_while = 0
    iteration = 1

    while iteration < 11:
        sum_1_to_10_while += iteration
        iteration += 1

    return sum_1_to_10_while

# test code
# print(one_to_ten_while())


def one_to_thousand_while():
    """
    This function sums up integers 1 to 1000 using 'while' loop, and returns the sum.
    """
    sum_1_to_1000_while = 0
    iteration = 1

    while iteration < 1001:
        sum_1_to_1000_while += iteration
        iteration += 1

    return sum_1_to_1000_while

# test code
# print(one_to_thousand_while())


def one_to_thousand_odd_while():
    """
    This function sums up odd integers from 1 to 1000 using 'while', and returns the sum. 
    """
    sum_1_to_1000_odd_while = 0
    iteration = 1

    while iteration < 1001:
        if iteration % 2 == 1:
            sum_1_to_1000_odd_while += iteration
            iteration += 1
        else:
            iteration += 1

    return sum_1_to_1000_odd_while

# test code
# print(one_to_thousand_odd_while())


def mysqrt(a):
    """
    This function returns the approximate square root value of 'a' using arbitrary estimate 'x' (defined as 1 within this function). This will be repated until there is only a marginal difference between the 2 consecutive estimates.
    """
    x = 1
    epsilon = 0.00000000000001

    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y

    return y


# test code
# print(mysqrt(2))

def test_square_root():
    """
    Set a value of 'a', up to which this function returns the square root value using 'mysqrt(),' 'math.sqrt()', and the difference between them. Tabulate the values in each column and returns the table. 
    """
    a = 1
    table = list()

    while a < 10:
        table.append(
            [float(a), mysqrt(a), math.sqrt(a), math.sqrt(a)-mysqrt(a)])
        a += 1

    return table


print(tabulate(test_square_root(), headers=[
      'a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'], numalign='left', floatfmt=('.1f', "", "", "")))

# alternative approach

def test_square_root_for_loop():
    """
    Using a 'for' loop, retrieve
    """

    table = list()

    for i in range(1, 10):
        table.append(
            [float(i), mysqrt(i), math.sqrt(i), math.sqrt(i)-mysqrt(i)])
    
    return table

# test code

print()
print(tabulate(test_square_root_for_loop(), headers=[
      'a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'], numalign='left', floatfmt=('.1f', "", "", "")))