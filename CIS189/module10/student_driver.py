"""
* Name         : M10 T3: Unit Tests for a Class Assignment(Driver class)
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Driver class for the student class to print student info.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
from student_class import Student


if __name__ == "__main__":
    student1 = Student("Goche", "Noah", "CIS", 4.0)
    student2 = Student("Doe", "John", "ABC", 0.0)

    print(str(student1))
    print(str(student2))
