"""
* Name         : <hourly_employee_input2.py>
* Author       : <Noah Goche>
* Created      : <6/17/2026>
* Course       : CIS189
* IDE          : <Visual Studio Code>
* Description  : <The program uses a function for reading user's name, hourly pay, and hours worked and a function for finding 
                  the weekly pay and then print the user's name, hours worked, and weekly pay.>
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def hourly_employee_input ():
    """Prompts the user for their name, hours worked, and hourly pay rate to calculate the weekly pay then print 
    their name, hours worked, and weekly pay. """
    name = input("Enter name: ")
    assert (name.isalpha()), f"Name must have apha characters only"

    hours_worked = int(input("Enter hours worked: "))
    assert (hours_worked > 0), f"Hours worked must be greater than 0"
    
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    assert (hourly_pay_rate > 0), f"Pay must be greater than 0"

    week_pay = weekly_pay(hours_worked, hourly_pay_rate)
    
    print("Name: {}, hours worked {}, weekly pay {}".format(name, hours_worked, week_pay))

def weekly_pay (hours_worked, hourly_pay_rate):
    """calculates the total weekly pay"""
    weekly_pay = hours_worked * hourly_pay_rate
    return weekly_pay
     


if __name__ == '__main__':
        try: 
            hourly_employee_input()  
        except ValueError as value_error:  
            print("ValueError")
        except AssertionError as assertion_error:
            print(assertion_error)

