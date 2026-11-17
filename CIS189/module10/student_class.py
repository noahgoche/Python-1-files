"""
* Name         : M10 T3: Unit Tests for a Class Assignment(Student)
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Student class holds last name, first name, major, and gpa with a str method
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        if (not lname.isalpha() or not fname.isalpha() or not major.isalpha() or (not isinstance(gpa, float) or not (0 <= gpa <= 4.0))):
            raise ValueError
            
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa
     
        
       
       
        
        # if (not isinstance(gpa, float) and not (0 <= gpa <= 4.0)):
        #     raise ValueError
        
        


    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)