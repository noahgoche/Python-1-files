"""
* Name         : M5 T2: Input Validation while Loops Assignment
* Author       : Noah Goche
* Created      : 6/24/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Prompts user for a number from 1-100 until the user enters
a valid number then prints the number and amount of tries it took for valid input. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def pick_number():
    """Takes an integer from the user and prints the value and number of tries
    it took to get a value from 1-100.
    :Returns void
    :Raises Value Error when a non number value is given by the user
    :Raises Assertion Error if the value is not within 1-100"""

    input_invalid = True
    try_count = 0

    while(input_invalid == True):
        try_count+=1
        try:
            user_number = int(input("Enter a number from 1 to 100: "))
            assert (0 < user_number < 101)
        except ValueError, AssertionError:
            print("Invalid input, try again.")
        else:
            input_invalid = False
            print("specified value = {}, number of tries = {}".format(user_number, try_count))

if __name__ == '__main__':
    pick_number()
