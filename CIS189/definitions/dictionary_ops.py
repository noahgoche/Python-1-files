"""
* Name         : M9 T1: Python Package Assignment(Dictionary_ops)
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Module has a function to take a dictionary then print the key value pairs
one line at a time.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""


def print_dict(user_dict):
    """Prints the key and value from the provided dictionary one at a time per line
    Param: user_dict is a dictionary provided by the user to be printed
    """
    for key, val in user_dict.items():
        print("Key: {}, Value{}".format(key, val))