"""
* Name         : M9 T1: Python Module Assignment
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Module that holds functions to print a greeting, the author of the code, the key and value
of a user provided dictionary, and the values from a user provided set.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""


def print_greeting():
    """Prints a friendly greeting
    """
    print("Hello, how are you?")


def print_author():
    """Prints me, Noah, as the author of this module
    """
    print("Noah Goche is the author of this module.")

def print_dict(user_dict):
    """Prints the key and value from the provided dictionary one at a time per line
    Param: user_dict is a dictionary provided by the user to be printed
    """
    for key, val in user_dict.items():
        print("Key: {}, Value{}".format(key, val))

def print_set(user_set):
    """Prints every value on one line at a time from user_set
    Param: user_set is a set provided by the user to print every value
    """
    for value in user_set:
        print(value)