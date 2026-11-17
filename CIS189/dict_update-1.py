"""
* Name         : M8 T2: Dictionary Update Assignment
* Author       : Noah Goche
* Created      : 7/8/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Program loads a list of names and numbers into a dictionary with the name being
the key and the phone number being the value in the pair. Then prompts user for a new name and number
to add to the phone book dictionary. Finally prompts the user for an existing name to then update their
phone number. The program then prints the update dictionary out. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def main():
    """
    Create a phone book for the names and numbers in the given lists.
    The follow the instructions in the comments. 
    """

    names = ["juan", "michael", "steve", "jimmy", "tony", "merle", "willie"]

    numbers = ["708-555-9878", "630-555-0009", "630-555-1112", "515-555-9999", 
               "847-555-4443", "312-555-9823", "414-555-6767"]
    
    # --------------------------------------------------------------------------
    # TODO: Create an empty dictionary. Iterate over names and numbers, 
    # creating a dictionary that maps names to numbers. 
    # Hint: Look into to using thew zip function to iterate over names 
    # and numbers as a list of 2-tuples.
    #---------------------------------------------------------------------------
    phone_book = {}
    
    phone_and_names = zip(names, numbers)

    for i in phone_and_names:
        phone_book [i[0]] = i[1]


    #---------------------------------------------------------------------------
    # TODO: Prompt user for a name NOT in your dictionary (continue to prompt 
    # user until they enter a name not already in the dictionary). Once a new 
    # name is provided, prompt for a phone number. Then add the key-value pair 
    # to your dictionary.
    #---------------------------------------------------------------------------
   
    loop = True
    while(loop):
        name = input("Enter a new name: ")
        if name not in phone_book:
            loop = False
            number = input("Enter a phone number: ")
            phone_book [name] = number
        else:
            print("Invalid input")


    #---------------------------------------------------------------------------
    # TODO: Prompt user for a name in your dictionary (continue to prompt 
    # user until they enter a name already in the dictionary). Once an existing
    # name is provided, prompt for a new phone number, and update the dict
    # with the new number. 
    #---------------------------------------------------------------------------
    loop = True
    while(loop):
        name = input("Enter an existing name: ")
        if name in phone_book:
            loop = False
            number = input("Enter a new phone number: ")
            phone_book [name] = number
        else:
            print("Invalid input")

   
    #---------------------------------------------------------------------------
    # TODO: Print dictionary with new name/number and updated number. 
    # --------------------------------------------------------------------------
    print(phone_book)


if __name__ == "__main__":
    main()
