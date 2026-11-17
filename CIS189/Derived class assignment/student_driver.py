"""
* Name         : M11 T2:Derived Class Assignment
* Author       : Noah Goche
* Created      : 7/22/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Driver class for testing student class
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
from student import Student

def main():
    # Driver
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student

if __name__ == '__main__':
    main()