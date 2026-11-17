"""
* Name         : M11 T2:Derived Class Assignment
* Author       : Noah Goche
* Created      : 7/22/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Person class that creates a person with the attributes first name, last name, and address and can display them
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):   
        self._last_name = lname
        self._first_name = fname
        self._address = addy


    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address  