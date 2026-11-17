"""
* Name         : M11 T1: Class Composition Assignment
* Author       : Noah Goche
* Created      : 7/22/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Creates computer object using memory and diskspace classes and prints the computer objects in main
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

"""
CIS189 Module 11 Composition assignment script.
"""
import random
from datetime import datetime

# Do not modify.
class Memory:
    """
    Class representation of computer memory.
    """
    def __init__(self):

        self.total_ram_gb = 16

    def available(self):
        in_use = random.uniform(0, self.total_ram_gb)
        avail = self.total_ram_gb - in_use 
        return avail


# Do not modify.
class DiskSpace:
    """
    Class representation of computer hard disk storage.
    """
    def __init__(self):
        self.total_capacity_gb = 512

    def available(self):
        in_use = random.uniform(0, self.total_capacity_gb)
        avail = self.total_capacity_gb - in_use 
        return avail



class Computer:
    """
    Computer class. 
    
    Attributes:
        name: str
            Passed in as an argument to the constructor. 
        

    Methods: 
        get_info:
            Returns a string of the form:

            [timestamp] computer name: <name>, available memory: <available memory>, available storage: <available storage>
    
    """

    def __init__(self, name):
        self.name = name
        self.diskSpace = DiskSpace()
        self.memory = Memory()


    def get_info(self):
        """
        Returns the current time, name, available memory, and available storage of the computer
        """
        return (str(datetime.now().strftime("%H:%M:%S")) + ": computer name: " + self.name + ", available memory: " + f"{self.memory.available():.2f}gb, available storage: " + f"{self.diskSpace.available(): .2f}gb")


def main():

    machine_names = ["RQS445", "MIKES-MACHINE", "Leet-315"]

    # For each of the machine_names, create an instance of the Computer
    # class, then call `get_info` for each. 
    for name in machine_names:
        comp = Computer(name)
        print(comp.get_info())
        del comp



if __name__ == '__main__':
    main()