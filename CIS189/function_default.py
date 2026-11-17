"""
* Name         : M6 T1: Functions Default Values Assignment
* Author       : Noah Goche
* Created      : 7/1/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Program tests the score_input function that takes a name, score, and invalid message from the user and returns
                 the name and score if the value is between 0 and 100 or the invalid message. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def score_input(test_name, test_score=-1, invalid_message='Invalid test score!'):
    """Takes a required input for the name of the test, optional score and invalid_message from the user
    then prints the invalid message if the test score value is not in between 0 and 100
    :Returns the test name and score if the input is valid otherwise it returns the invalid_message
    :Raises Value Error when a non number value is used for the test_score
    :Raises Assertion Error if the test score is less than 0 or greater than 100"""
    try:
        score = int(test_score)
        assert (0 < score < 101)
    except (AssertionError):
        return(invalid_message)
    except ValueError as value_error:
        return("ValueError encountered!")
    else:
        output_message = ("{} Score: {}".format(test_name, score))
        return output_message
    

if __name__ == '__main__':
    #Good input
    display_string = score_input('Test 1', 70)  
    print(display_string)

    #Below range test
    display_string = score_input('Test 2', -10)
    print(display_string)

    #Above range test
    display_string = score_input('Test 2', 1000)
    print(display_string)

    #Non numeric test
    display_string = score_input('Test 2', "test")
    print(display_string)