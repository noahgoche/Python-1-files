"""
* Name         : M10 T1: Encapsulation Assignment
* Author       : Noah Goche
* Created      : 7/16/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Class that creates Employee objects containing their first and last name, address, phone number, salary, and start date. Includes a display function
that outputs their information and is used in main. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
"""
CIS189 Module 10 Encapsulation assignment script.
"""

class Employee:
    """
    Employee class.
    """
    def __init__(self, last_name, first_name, address = "", phone_number = "", salary = "", start_date = ""):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.salary = salary
        self.start_date = start_date


    def display(self):
        """
        Display employee information as:

            LAST_NAME, FIRST_NAME: <last name, first name here>
            PHONE_NUMBER: <phone number here>
            ADDRESS: <address here>
            START DATE: <start date here>
            SALARY: <salary here>
        """
        return ("LAST_NAME, FIRST_NAME: " + str(self.last_name) + ", " + str(self.first_name) + "\n" + "PHONE_NUMBER: " + str(self.phone_number) + "\n" + "ADDRESS: " + str(self.address) 
        + "\n" + "START DATE: " + str(self.start_date) + "\n" + "SALARY: " + str(self.salary))


def main():

    person_list = [
        {"last_name": "VanRossum", "first_name": "Guido","address": "461 Ocean Blvd",
        "phone_number": "773-735-1849", "salary": 97500, "start_date": "1991-02-22"},

        {"last_name": "Haggard", "first_name": "Merle","address": "Bakersfield, CA",
        "phone_number": "484-765-2231", "salary": 72500, "start_date": "1967-11-08"},

        {"last_name": "Prine", "first_name": "John","address": "Paradise, KY",
        "phone_number": "743-435-8310", "salary": 88500, "start_date": "1995-07-31"},
        ]
    
   
    # Iterate over person_list, and create a new Employee instance and call the 
    # display method for each.
    for person in person_list:
        #takes the dictionary key values as keyword args to create each employee object then adds to a list of employees then prints the display function
        new_Employee = Employee(**person)
        print(new_Employee.display() +"\n")       
        del new_Employee



if __name__ == "__main__":

    main()

