import time
# print(time.time_ns())
# avoid precision loss

# ex03
# The time module provides a function, also named time, that returns the current Greenwich Mean Time in
# “the epoch, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.

# Write a script that reads the current time and converts it to a timeminute of day in hours, minutes, and seconds,
# plus the number of days since the epoch. You can only use time module.

# time.time_ns() = 0 -> January 1, 1970, 00:00:00 (UTC)
# GMT and EST?

# current time of GMT in seconds since January 1 of 1970, 00:00:00 (UTC)
# There is no time difference between GMT and UTC

current_time_seconds = int(time.time_ns() / 1e9 // 1)
# Decided not to use rounding since the time does not come until it has fully reached
# print(current_time_seconds, time.time())

# convert up to different units step by step
# to minutes

minutes_split = divmod(current_time_seconds, 60)
seconds_final = minutes_split[1]
minutes_component = minutes_split[0]
# print(minutes_component, seconds_final)

# to hours
hours_split = divmod(minutes_component, 60)
minutes_final = hours_split[1]
hours_component = hours_split[0]
# print(hours_component, minutes_final, seconds_final)

# to days
days_split = divmod(hours_component, 24)
hours_final = days_split[1]
days_component = days_split[0]
print(days_component, hours_final, minutes_final, seconds_final)

# The number of days which have passed since the epoch time
# (days_component)

print(f'It has been {days_component} days since the epoch date of January 1st, 1970.\nThe current time is {hours_final:0>2d}:{minutes_final:0>2d}:{seconds_final:0>2d} GMT.')
