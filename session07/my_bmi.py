# ex-01.2
# Write a function, calculate_bmi that takes two parameters, weight and height, to return BMI value. Write another function, get_bmi_category that prompts user to input values for weight and height, converts them to floats, uses calculate_bmi to calculate BMI value, and returns the corresponding BMI category.

def calculate_bmi(weight, height):
    """Take weight and height and return BMI in metric measure."""

    # weight in kilograms
    # height in meters

    bmi = weight / height**2

    return bmi

# print(calculate_bmi(60, 1.82))


def get_bmi_category():
    """Convert numerical bmi to a categorical value"""

    bmi_numbers_input = input(
        'Input your weight in kg and height in m in the order, with a comma and a space in between.\ni.g. 60, 1.82 >>> ')

    bmi_list = list()
    bmi_list = bmi_numbers_input.split(', ')

    for i in range(len(bmi_list)):
        bmi_list[i] = float(bmi_list[i])

    resultant_bmi = calculate_bmi(bmi_list[0], bmi_list[1])

    if resultant_bmi < 18.5:
        return 'BMI Category: Underweight'
    elif resultant_bmi < 25:
        return 'BMI Category: Normal weight'
    elif resultant_bmi < 30:
        return 'BMI Category: Overweight'
    else:
        return 'BMI Category: Obesity'


print(get_bmi_category())
