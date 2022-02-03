# Functions
#  
# 

# def gd():
#     print('Beginning of Groundhog day...')
#     import time
#     time.sleep(1)
#     print('End of Groundhog day.')
#     time.sleep(.2)
#     gd()

# gd()

# ctl + C to break the current loop

# screenshot: windows key + shift + S
# screenrecord: webex/zoom, obs, powerpoint -> insert + screenrecord

# value = None vs. value = ""
# value = None vs. value = 0
# the former incomputable, the latter computable
# always some character after backward slash
import random
from re import X
# print(random.random()*10)

# year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# pseudo-code or docstrings
# declare variables for constants, use uppercases for constant
# % == get remainder, // == extract integer part

r1 = 123
r2 = 567
r3 = 10000000

# a1 = 3.14159 * r1 * r1
# a2 = 3.14159 * r2 * r2
# a3 = 3.14159 * r3 * r3

# print(a1, a2, a3)

def area_of_circle(x):
    """print the area of a circle, given the radius value"""
    # docstring required in order to be recognized when hovering upon
    # detect the type of x
    # If x is one float
    area = 3.14159265 * x * x
    print(area)
    # If x is a list
    # 

# def area_of_circles(radius):
#     for r in radius:
#         area_of_circle(r)


# area_of_circle(r1)   # call the function
# area_of_circle(r2) 
# area_of_circle(r3) 

# rs = {r1, r2, r3}
# area_of_circles(rs)

print(ord('K'))
print(chr(75))
print(ord("航"))
# print(chr(-1)) does not work, has to be between 0 and 110000
# math.floor
# math.ceil
# unicode

#module.function(argument)

