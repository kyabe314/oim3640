import math

#ex02-01
#How many seconds are there in 42 minutes 42 seconds?

#Separate the given time into minutes component and seconds component
#Convert and minutes component into seconds for the unit specified
#in the question
#1 minute = 60 seconds

minutes_component = 42                                   #minutes
minutes_to_seconds = minutes_component*60              #seconds
seconds_component = 42                                   #seconds
seconds_total = minutes_to_seconds+seconds_component   #seconds

#change datatype for print function
seconds_total_str = str(seconds_total)

#print(seconds_total) 
#in order to verify the result

#Print the result for human readability
print('A1. '+'There are '+seconds_total_str+' seconds in 42 minutes and 42 seconds.')


#ex02-02
#How many miles are there in 10 kilometers?

#Multiply kilometers by miles/kilometers for unit convertion to miles
#1 mile = 1.61 kilometers

dist_in_kilos = 10                              #kilometers
kilos_to_miles = 1/1.61                         #conversion rate (miles/kilometers)
dist_in_miles = dist_in_kilos*kilos_to_miles  #miles

#print(dist_in_miles)
#in order to verify the result
#Uncomment this function for the answer with extended decimal places

#round the result to two decimal places for human readability
dist_in_miles = round(dist_in_miles,2)

#change the datatype for print function
dist_in_miles_str = str(dist_in_miles)

#Print the result for human readability
print('A2. '+'There are about '+dist_in_miles_str+' miles in 10 kilometers.')


#ex02-03
#If you run a 10 kilometer race in 42 minutes 42 seconds, 
#what is your average pace (time per mile in minutes and seconds)? 

#For pace, first calculate seconds/miles to avoid unit complications
#Next, extract minutes from seconds by dividing the pace by 60 and rounding it down
#Finally, subtract the seconds which were converted to minutes to get the seconds component of the pace

pace_in_seconds = seconds_total/dist_in_miles                               #seconds/miles for preliminary pace converstion

#print(pace_in_seconds)
#in order to verify the result

pace_minutes_component = math.floor(pace_in_seconds/60)                     #minutes
pace_seconds_component = pace_in_seconds-pace_minutes_component*60      #seconds
pace_seconds_component = int(math.floor(pace_seconds_component))            #seconds, rounded down to avoid overrepresentation

#print(pace_minutes_component)
#print(pace_seconds_component)
#in order to verify each component

#change the datatype for print function
pace_minutes_component_str = str(pace_minutes_component)
pace_seconds_component_str = str(pace_seconds_component)

#Print the result for human readability
print('A3. '+'The average pace is '+pace_minutes_component_str+' minutes and '+pace_seconds_component_str + ' seconds per mile.')

#What is your average speed in miles per hour?

#average speed = distance traveled/time = change in position with respect to time = dp/dt
#Convert total travel time in seconds to hours, and divide distance traveled in miles by the hours
#1 hour = 60 minutes * 60 seconds = 3600 seconds

seconds_to_hours = seconds_total/3600   #hours
dpdt = dist_in_miles/seconds_to_hours   #miles/hour

#print(dpdt)
#in order to verify the result

#Round down to two decimal places to avoid overrepresentation and
#for human readability
dpdt = math.floor(dpdt*100)/100

#print(dpdt)

#change the datatype for print function
dpdt_str = str(dpdt)

#Print the result for human readability
print('    '+'The average speed is '+dpdt_str+' miles per hour.')
