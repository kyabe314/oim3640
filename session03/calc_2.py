import math

# Alt + Shift + F = Formatting

# ex02-01
# What is the volume of a sphere with r = 5?
#
# The volume of a sphere with radius "r" is the following:
# (4/3)*pi*r^3

# Assign radius length
radius = 5

# Calculate the volume of the sphere
volume_sphere = (4/3) * math.pi * radius ** 3

print(
    f'A1. The volume of sphere with the radius of {radius} is {volume_sphere:.2f} centimeter cubed.')

# ex02-02
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

cover_price = 24.95
discount_rate = 0.4
discounted_price = cover_price * (1 - discount_rate)

shipping_cost_first = 3
shipping_cost_additional = 0.75

number_of_copies = 60

books_total = discounted_price * 60
shipping_total = shipping_cost_first + \
    shipping_cost_additional * (number_of_copies - 1)

cost_total = books_total + shipping_total

print(
    f'A2. The total whole sale cost for {number_of_copies} copies is {cost_total:.2f} dollars.')

# ex02-03
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?

hour_component_depature = 6  # hours
minute_component_depature = 52  # minutes
second_component_depature = 0  # seconds

minutes_easy = 8     # minutes
minutes_tempo = 7    # minutes

# Convert seconds to minutes

seconds_easy = 15
seconds_tempo = 12
seconds_to_minutes = 1/60

decimal_easy = seconds_easy * seconds_to_minutes
decimal_tempo = seconds_tempo * seconds_to_minutes

minutes_easy_pace = minutes_easy + decimal_easy
minutes_tempo_pace = minutes_tempo + decimal_tempo

# print(minutes_easy_pace, minutes_tempo_pace)

miles_easy = 1 + 1
miles_tempo = 3

minutes_easy_total = minutes_easy_pace * miles_easy
minutes_tempo_total = minutes_tempo_pace * miles_tempo

minutes_total = minutes_easy_total + minutes_tempo_total

# print(minutes_total)

minute_component_arrival = minute_component_depature + minutes_total
minute_component_split = divmod(minute_component_arrival, 60)
minute_component_arrival = minute_component_split[1]

hour_component_arrival = hour_component_depature + minute_component_split[0]
hour_component_arrival = int(hour_component_arrival)

# print(minute_component_split)
# print(minute_component_arrival, hour_component_arrival)


second_component_arrival = second_component_depature + \
    minute_component_arrival % 1    # in minutes
second_component_arrival_rounded = round(second_component_arrival * 60)

minute_component_arrival = int(
    minute_component_arrival - second_component_arrival)

# print(second_component_arrival)

print(
    f'A3. You will get home at {hour_component_arrival:0>2d}:{minute_component_arrival:0>2d}:{second_component_arrival_rounded:0>2d} am for breakfast.')

# ex02-04
# If my average grade rises from 82 to 89.
# What is the percentage of the increase? Format the result as xx.x%.
# Keep one figure after decimal point.

grade_avg_before = 82
grade_avg_after = 89
percentage_change = (grade_avg_after / grade_avg_before - 1) * 100

print(f'A4. The percentage of the increase is {percentage_change:.1f} %.')


