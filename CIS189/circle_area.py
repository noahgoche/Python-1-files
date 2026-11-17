"""
* Name         : <circle_area.py>
* Author       : <Noah Goche>
* Created      : <6/17/2026>
* Course       : CIS189
* IDE          : <Visual Studio Code>
* Description  : <Program takes a radius value from the user and returns the area of the circle>
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""


# Must include a docstring describing the functionality, the parameter and return type
# Must include a try/except block to handle cases when input radius is not a numeric type. If input type is invalid, function should return -1
# Your print / output must be done in a function named main
# Evaluate your function against the following radius values:

# 1
# 5.33
# 7.5
# 10
# "thirty"
# Submit a .py 

def get_area():
    """Takes a float from the user as a radius value to solve for the circle area
    :Returns the area based off the given radius or -1 if the input is invalid
    :Raises Value Error when a non number value is used as the radius
    :Raises Assertion Error if the radius is negative"""

    try:
        radius = float(input("Enter the radius: "))
        assert (radius > 0)
    except ValueError, AssertionError:
        print("Invalid input")
        return -1
    
    PI = 3.14
    circle_area = radius**2 * PI

    return circle_area

if __name__ == '__main__':
       
    area = get_area()
print("The area of the circle is {}".format(area))
