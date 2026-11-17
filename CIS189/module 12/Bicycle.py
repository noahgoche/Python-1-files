"""
* Name         : M12 T3: Abstract Class Assignment(Bicycle)
* Author       : Noah Goche
* Created      : 7/26/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Subclass of Rider that has information for a bicycle
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from Rider import Rider

class Bicycle(Rider):
    def __init__(self):
        self.num_riders = "1 or 2 if tandem or a daredevil"
        self.ride_type = "Human powered, not enclosed"

    def riders(self):
        return self.num_riders

    def ride(self): 
        return self.ride_type

