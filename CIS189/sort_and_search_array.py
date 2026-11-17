"""
* Name         : M8 T4: Search and Sort Arrays Assignment
* Author       : Noah Goche
* Created      : 7/8/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Program that uses the functions search_array and sort_array to take an array and search value and an array respectively
to return the index of the search value and sort the array. 
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import array

def search_array(arr, search_value):
    """Searches the given array for the specified value and returns the index if it exists and -1 if it doesn't
    :Param arr is the array to be searched
    :Param search_value is the value provided by the user to search within the array 
    """
    if search_value in arr:
        return arr.index(search_value)
    else:
        return -1


def sort_array(arr):
    """Sorts the provided array in ascending order
    :Param arr is the array to be sorted 
    """
    arr = array.array('i', sorted(arr))
    #returns arr after it has been sorted. Not returning the sorted array leaves it unsorted in main.
    return arr
    

if __name__ == '__main__':
    arr = array.array('i',[1, 4, 3, 2, 11, 5, 7])
    
    print(search_array(arr, 11))

    #Set arr = to the sorted version of arr
    arr = sort_array(arr)
    print(arr)
