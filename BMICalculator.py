# BMICalculator.py
# Your job is to write a BMI calculator that matches the formula
# and chart on http://flightphysical.com/medical-exam/weight
import math
# Define Function below
# be sure to return an integer
def calculateBMI(height, weight):
    bmi = (weight*703)/(height*height)
    bmi = round(bmi)
    return bmi

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function 
