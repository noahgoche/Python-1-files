"""
* Name         : M12 T3: Abstract Class Assignment(Driver)
* Author       : Noah Goche
* Created      : 7/26/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Driver class to test the creation and use of functions for car, motorcycle, and bicycle subclasses
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from Bicycle import Bicycle
from Motorcycle import Motorcycle 
from Car import Car

def main():
    bike = Bicycle()
    print(bike.ride())
    print(bike.riders())

    motorcycle = Motorcycle()
    print(motorcycle.ride())
    print(motorcycle.riders())

    car = Car()
    print(car.ride())
    print(car.riders())



if __name__ == '__main__':
    main()

    
    