"""
* Name         : M5 T1: Basic for Loops Assignment
* Author       : Noah Goche
* Created      : 6/23/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Prints a list of floating point numbers
*                using a for loop
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

float_list = [1.2, 3.4, 332.213, 3.23424, 212.2, 1.2345, 10.1, 9.0, 100.2]

print("Numbers from list of floating point numbers")
for num in float_list:
    print(num)

print("\nOdd numbers from 99 to 33")

#prints every odd number descending from 99 to 33 by using range() and a -2 for the step value
for odd_num in range(99, 31, -2):
    print(odd_num)