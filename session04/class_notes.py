import math  # import is a command, not a function
import random
# s1 = 'a'
# s2 = 'ab'
# s3 = 'abc'
# s4 = 'abcd'

# print(f'{s1:>10}')
# print(f'{s2:>10}')
# print(f'{s3:>10}')
# print(f'{s4:>10}')

# {:0>2d} add some zeros in front

# a_large_number = 10_000_0000
# {:2%}

# Data Types
# modules, statements, expressions, and objects

# a python file is a module i.g. calc.py

# Objects - numbers, strings, lists, dictionaries, tuples, files, sets, other core # types such as Boolean, types, None

# tuples are immutable

# print(3.14e-2)
# print(len(str(2 ** 1_000_000)))

# print(math.pi)
# print(random.random())

# print('I\'m ok') 
# backward slash in order to include a quotation mark in a print statement

# print('I\'m learning \nPython.')

# print('\\\n\\')
# the first backslash to normalize the second backslash into a string
# print('\\\\')

# print('''
# Multiple
# Lines
# ''')

# print(r'C:\user\documents')
# r lets us avoid escape characters

# in_China = False
# age = input('How old are you? >>> ')
# age = int(age)
# if age > 21 or in_China:
#     print('Yes, you can.')
# else:
#     print('No, you cannot.')

def f():
    print('hi')
    return 123

result = f()
print(result)



