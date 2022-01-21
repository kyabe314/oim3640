import math

#

#ex02-01
#How many seconds are there in 42 minutes 42 seconds?

#1 minute = 60 seconds
minutes_component = 42
minutes_to_seconds = minutes_component * 60
seconds_component = 42
seconds_total = minutes_to_seconds + seconds_component
#print(seconds_total)

#ex02-02
#How many miles are there in 10 kilometers?

#1 mile = 1.61 kilometers
dist_in_kilo = 10
kilo_to_mile = 1/1.61
dist_in_mile = dist_in_kilo * kilo_to_mile
#print(dist_in_mile)

#ex02-03
#If you run a 10 kilometer race in 42 minutes 42 seconds, 
#what is your average pace (time per mile in minutes and seconds)? 
#What is your average speed in miles per hour?

pace_in_seconds = seconds_total/dist_in_mile
#print(pace_in_seconds)
pace_minutes_component = math.floor(pace_in_seconds/60)
pace_seconds_component = pace_in_seconds - pace_minutes_component * 60
pace_seconds_component = int(round(pace_seconds_component, 0))
#print(pace_minutes_component)
#print(pace_seconds_component)

#speed = dp/dt = distance/time = change in position with respect to time
#1 hour = 60 minutes * 60 seconds = 3600 seconds
seconds_to_hours = seconds_total/3600
dpdt = dist_in_mile/seconds_to_hours
#print(dpdt)