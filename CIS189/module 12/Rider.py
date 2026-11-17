"""
* Name         : M12 T3: Abstract Class Assignment
* Author       : Noah Goche
* Created      : 7/26/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Abstract class that has methods for describing the ride and amount of riders for subclasses
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from abc import ABC, abstractmethod

class Rider(ABC): 

    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass

    