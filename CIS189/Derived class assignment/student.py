"""
* Name         : M11 T2:Derived Class Assignment
* Author       : Noah Goche
* Created      : 7/22/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Student class is a derived class of person and includes additional attributes; major, gpa,
student_id, and an overrided display function
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
from person import Person

class Student(Person):

    def __init__(self, student_id, lname, fname, major = 'Computer Science', gpa = '0.0', addy = ''):
        super().__init__(lname, fname, addy)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        

    def display(self):
        return super().display() + " (" + str(self.student_id) + ") " + self.major + " gpa: " + str(self.gpa)