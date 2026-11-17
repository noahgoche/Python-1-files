"""
* Name         : M8 T1: Set Assignment
* Author       : Noah Goche
* Created      : 7/8/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Code tests the function in_set that takes a value and a set as a parameter and prints whether the value is in the set
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def in_set(set, value):
    """Returns true if the value provided by the user is in the set also provided by the user
    Param: set is a set of string values provided by the user to be searched
    Param: value is the string value that is searched for in the set
    """
    if value in set:
      return True
    else:
       return False



if __name__ == '__main__':
    test_set = {"apple", "banana", "cherry"}
    test_value = "apple"

    if in_set(test_set, test_value):
        print("The value '{}' is in the set {}".format(test_value, test_set))
    else:
        print("The value '{}' is not in the set {}".format(test_value, test_set))

    test_value = 5

    if in_set(test_set, test_value):
        print("The value '{}' is in the set {}".format(test_value, test_set))
    else:
        print("The value '{}' is not in the set {}".format(test_value, test_set))

