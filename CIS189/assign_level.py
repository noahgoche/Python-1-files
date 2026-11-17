"""
* Name         : M8 T3: Selection using Dictionary Assignment
* Author       : Noah Goche
* Created      : 7/8/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Program uses a function which implements a dictionary to use for a case statement where a user provides a level parameter
and the function returns the corresponding amount of points
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def switch_level(level):
    """Takes a parameter, level, and returns the corresponding points associated with it
    Param: level, a capital character that is the key for the level dictionary
    Returns: The key value that corresponds to the level parameter from level_dict
    """
    level_dict = {'N': 50, 'B': 150, 'E': 300, 'A': 500}
    return level_dict.get(level, "Invalid Level")


if __name__ == '__main__':
    
    print("Novice level has {} points.".format(switch_level('N')))
    print("Beginner level has {} points.".format(switch_level('B')))    
    print("Experienced level has {} points.".format(switch_level('E')))
    print("Advanced level has {} points.".format(switch_level('A')))