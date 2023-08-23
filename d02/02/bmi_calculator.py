import sys

def user_input():
    height = input('enter your height in inches: ')
    weight = input('enter your weight in lbs: ')

    return convert_inches_to_meters(height), convert_pounds_to_kilos(weight)

def convert_inches_to_meters(height):
    return float(height) * 0.0254

def convert_pounds_to_kilos(weight):
    return float(weight) / 2.2046


if __name__ == "__main__":
    print('Welcome to the BMI Calculator \n')

    height, weight = user_input()
    print(f'Your BMI is: { int(weight / height ** 2) }')
