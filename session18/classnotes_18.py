# Debugging

try:
    number = int(input('Please enter a number: >>> '))
    result = 2022 / number
    print(result)
except ZeroDivisionError:
    print('You entered a zero')
except ValueError:
    print('You should enter a number')
finally:
    print('Whatever we do, we will always get here.')

print('Hello, world!')