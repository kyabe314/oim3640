# specify parameter name in the argument and you can change the order of the arguments!
# Python Tips
# if __name__ = "__main__":
#     main()
# def main():
#     test()

# To swap two variables
# b, a = a, b

# Use comparison chain:
# if 18.5 <= bmi <= 30:

# Whoever reads your code should be able to understand it without external reference.

# Iterations

# Calculate the sum of intergers from 1 to 1000

# result = 0

# for i in range(1, 1001):
#     print(f'Iteration {i}:')
#     print(f'Before adding {i}, current result is {result}.')
#     result += i
#     print(f'After adding {i}, result becomes {result}. \n')

# print(result)

def sum_odd():
    """"""
    result = 0

    for i in range(1, 1001):
        if i % 2 == 0:
            result += i

    return result

# print(sum_odd())

def sum_odd_2():
    result = 0
    for i in range(1, 10, 2):
        print(i)

# sum_odd_2()

# WHen to use for loop:
# 1. If we know exactly how many times we want to repeat
# 2. or we want to iterate over a sequence

# name = 'Rafael'

# for letter in name:
#     print(letter)

def countdown(n):
    while n > 0:
        print(n)
        import time
        time.sleep(1)

        n = n - 1
    
    print('Blastoff')

countdown(5)

# When to use while:
# only when we know when/what condition to stop

# Usually we use break in a if statement inside of loop.