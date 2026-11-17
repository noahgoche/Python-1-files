"""
* Name         : M6 T2: Inner Function Assignment
* Author       : Noah Goche
* Created      : 7/1/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.125.1
* Description  : Program uses nested functions to take a list of 1 or 2 values from the user
and calculate and return a String containing the perimeter and area
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

def measurements(a_list):
    """Takes a list and calculates the perimeter and area of a square or rectangle
    :Param a_list is a list of 1 or 2 
    :Returns a String containing the Perimeter and Area calculated from the list input vales"""

    def area(a_list):
        """Calculates the area of the shape with 1 value on the list finding the area of a square
        and 2 values on the list meaning the area is calculated for a rectangle
        :Param a_list is a list of 1 or 2 numbers 
        :Returns the area"""

        if len(a_list) == 1:
            area = a_list[0] * a_list[0]
        elif len(a_list) == 2:
            area = a_list[0] * a_list[1]
        return area 
    
    def perimeter(a_list):
        """Calculates the perimeter of the shape with 1 value on the list finding the perimeter of a square
        and 2 values on the list meaning the perimeter is calculated for a rectangle
        :Param a_list is a list of 1 or 2 numbers 
        :Returns the perimeter"""

        if len(a_list) == 1:
            perimeter = 4 * a_list[0]
        elif len(a_list) == 2:
            perimeter = 2 * a_list[0] + 2 * a_list[1]
        return perimeter 
    
    meas_area = area(a_list)
    meas_perimeter = perimeter(a_list)

    output = ("Permiter = {} Area = {}".format(meas_perimeter, meas_area))
    
    return output


if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)