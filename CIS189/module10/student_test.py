"""
* Name         : M10 T3: Unit Tests for a Class Assignment(Unit test)
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Unit tests for the student class.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import unittest
from student_class import Student

class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student("Doe", "John", "CIS", 3.5)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.major, "CIS")


    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.major, "CIS")
        self.assertEqual(self.student.gpa, 3.5)
    
    def test_student_str(self):
        self.assertEqual(str(self.student), "Doe, John has major CISwith gpa: 3.5")

    def  test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student2 = Student("345", "Johnny", "CIS", 123)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student3 = Student("Test", "123", "CIS", 3)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student3 = Student("Test", "Johnny", "123", 3)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student3 = Student("Test", "Johnny", "CIS", -1)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student3 = Student("Test", "Johnny", "CIS", "b")
    

if __name__ == '__main__':
    unittest.main()
