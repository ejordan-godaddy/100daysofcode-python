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
    bmi = int(weight / height ** 2)
    print(f'Your BMI is: { bmi } \n')
    
    if bmi <= 18.5:
        print('You are underweight')
    elif bmi <= 25 and bmi > 18.5:
        print('You have a normal weight')
    elif bmi <= 30 and bmi > 25:
        print('You are overweight')
    elif bmi <= 35 and bmi > 30:
        print('You are obese')
    elif bmi > 35:
        print('You are clinically obese')
