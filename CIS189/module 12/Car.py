"""
* Name         : M12 T3: Abstract Class Assignment(Car)
* Author       : Noah Goche
* Created      : 7/26/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Subclass of Rider that has information for a car
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from Rider import Rider

class Car(Rider):
    def __init__(self):
        self.num_riders = "1 plus comfortably"
        self.ride_type = "Engine powered, enclosed"

    def riders(self):
        return self.num_riders
    
    def ride(self): 
        return self.ride_type