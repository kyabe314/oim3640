# ex-02.1
# Write a program, factorial.py to compute a factorial of an integer, n.

def factorial (n):
    """Take an integer n as an input and return a factorial of the integer"""
    
    factorial_list = list()
    for i in range(n):
        if n <= 0:
            pass
        else: 
            factor = n - 1
            test = n % factor
            if test == 0:
                factorial_list.append(test)
            else:
                pass
