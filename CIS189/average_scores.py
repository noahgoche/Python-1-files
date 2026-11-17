"""
* Name         : <average_scores.py>
* Author       : <Noah Goche>
* Created      : <6/16/2026>
* Course       : CIS189
* IDE          : <Visual Studio Code>
* Description  : <The code takes a user's name, age, and three scores out of a hundred
                  and stores the average score.>
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

average_score = 0
NUMBER_OF_SCORES = 3

#Takes strings from the user for first and last name and tests whether they only contain alpha characters and returns an error otherwise
try:
   first_name = input("Enter your first name: ")
   assert (first_name.isalpha()), f"Your name may only contain alpha characters."
except AssertionError as assertion_error:
    print(assertion_error)

try:
   last_name = input("Enter your last name: ")
   assert (first_name.isalpha()), f"Your name may only contain alpha characters."
except AssertionError as assertion_error:
    print(assertion_error)

#takes user input for age and returns an error if the value is less than 0 or not an integer
try:
    age = int(input("Enter age: "))
    assert (age > 0), f"Your age must be greater than 0."
except AssertionError as assertion_error: 
    print(assertion_error)
except ValueError as value_error:
    print("Age must be an integer")

#takes user input for scores and returns an error if the value is less than 0 or not an integer
try:
    scores = int(input("Enter first score: "))
    assert (0 <= scores <= 100), f"The score must be greater than or equal to 0 and less than or equal to 100."
except AssertionError as assertion_error:
    print(assertion_error)
except ValueError as value_error:
    print("Scores must be integers")

try:
    score2 = int(input("Enter second score: "))
    assert (0 <= score2 <= 100), f"The score must be greater than or equal to 0 and less than or equal to 100."
except AssertionError as assertion_error:
    print(assertion_error)
except ValueError as value_error:
    print("Scores must be integers")
else:
    scores += score2

try:
    score3 = int(input("Enter third score: "))
    assert (0 <= score3 <= 100), f"The score must be greater than or equal to 0 and less than or equal to 100."
except AssertionError as assertion_error:
    print(assertion_error)
except ValueError as value_error:
    print("Scores must be integers")
else:
    scores += score3

average_score = float(scores/NUMBER_OF_SCORES)

#returns the user's information and average score rounded to two decimal places
print("{}, {} age: {} average grade: {:.2f}".format(last_name, first_name, age, average_score))