"""
* Name         : M9 T1: Python Package Assignment(Set_ops)
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Module has a function to take a set then print the values one line at a time.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def print_set(user_set):
    """Prints every value on one line at a time from user_set
    Param: user_set is a set provided by the user to print every value
    """
    for value in user_set:
        print(value)