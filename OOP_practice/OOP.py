class Point:
    """Represents a point in 2-D space"""





my_point = Point()
# print(my_point)

# print(type(my_point))
# print(isinstance(my_point, Point))

# You can assign values to an instance using a dot notation

my_point.x = 3
my_point.y = 4

# print(my_point.x)
# print(my_point.y)

# my_point.y
# "Go to object my_point and get the value of y"

def point_print(p):
    print(f'({p.x}, {p.y})')

print(point_print(my_point))


class Time:
    """Represents the time of the day
    
    attributes: hour, minute, second
    """
    

time = Time()
time.hour = 1
time.minute = 31
time.second = 30

# pure function 

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

def print_time(t):
    print(f'{t.hour}:{t.minute}:{t.second}')

start = Time()
start.hour = 9
start.minute = 45
start.second =  0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
# print_time(done)

# modifier


