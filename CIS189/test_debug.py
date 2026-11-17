"""
* Name         : M5 T4: Debugging in Python
* Author       : Noah Goche
* Created      : 6/24/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : . 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def print_to_number(number):
    """Prints to the number value passed in, beginning at 1"""
    for counter in range(1,number):
        print (counter)

if __name__ == '__main__':
    print_to_number(10)