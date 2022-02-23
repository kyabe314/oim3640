# ex-01.1.1
# Write a function named check_fermat that takes four parameters — a, b, c and n — and checks to see if Fermat’s theorem holds.

import time

def check_fermat(a, b, c, n):
    """Take positive integers for a, b, c, and make them to the power of n. This function tests to see if the Fermat's Last Themrem really holds."""
    if n > 2 and a ^ n + b ^ n == c ^ n:
        print('Holy smokes, Fermat was wrong!')
    elif n <= 2:
        print('Outside of the range of the theory.')
    else:
        print('No, that doesn\'t work.')


# check_fermat(3, 4, 5, 3)


# Write another function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.

def input_fermat():
    """Take an input for each argument from a user, and apply them and test those values o check_fermat function."""
    
    time.sleep(1)

    print('Fermat\'s Last Theorem states that \nthere are no posistive integers a, b, c that satisfy a^2 + b^2 = c^2 when n is greater than 2.')
    time.sleep(2)

    print('Put your own set of numbers in to see if that really holds!')
    time.sleep(2)

    numbers_input = input('Input numbers in the order of a, b, c, and n, with a comma and a space in between.\ni.g. 1, 2, 3, 2. >>> ')

    input_list = list()
    input_list = numbers_input.split(', ')
    # print(input_list)

    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
        
    check_fermat(input_list[0], input_list[1], input_list[2], input_list[3],)


input_fermat()
