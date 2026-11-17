"""
* Name         : <if_elif_testing>
* Author       : <Noah Goche>
* Created      : <6/10/2026>
* Course       : CIS189
* IDE          : <Visual Studio Code>
* Description  : <Returns the price of the level for a Programmer's Toolkit Monthly Subscription Box
*                 based off of user input selecting the level they want.>
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

level = input("Enter the level you want to purchase: ")

if level == "Platinum":
    print("The cost is $60")
elif level == "Gold":
    print("The cost is $50")
elif level == "Silver":
    print("The cost is $40")
elif level == "Bronze":
    print("The cost is $30")
else:
    print("The cost is free")