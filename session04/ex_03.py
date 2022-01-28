import time
# print(time.time_ns())
# avoid precision loss

# ex03
# The time module provides a function, also named time, that returns the current Greenwich Mean Time in 
# “the epoch, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.

# Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, 
# plus the number of days since the epoch. You can only use time module.

# time.time_ns() = 0 -> January 1, 1970, 00:00:00 (UTC)
# GMT and EST?

# current time of GMT in seconds since January 1 of 1970, 00:00:00 (UTC)
# There is no time difference between GMT and UTC

current_time_seconds =int(time.time_ns() / 1e9 // 1)
# Decided not to use rounding since the time does not come until it has fully reached
print(current_time_seconds, time.time())

# convert up to different units step by step
# to minutes