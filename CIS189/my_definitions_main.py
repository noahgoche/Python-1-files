"""
* Name         : M9 T1: Python Module Assignment(Main)
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Main class used to test the my_definitions module
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
import my_definitions as definitions

if __name__ == "__main__":
    definitions.print_greeting()
    definitions.print_author()

    test_dict = {"first": "val1", "second": "val2", "third": "val3"}

    definitions.print_dict(test_dict)

    test_set = {"setVal1", "setVal2", "SetVal3", "SetVal4"}

    definitions.print_set(test_set)
    