"""
* Name         : Final Project Overview (Player base class)
* Author       : Noah Goche
* Created      : 8/3/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.132.1
* Description  : Base class containing player constructor, getters, setters, and methods for player characters in a video game.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from datetime import datetime

class Player:
    """
    Generic Player Class
    """
    def __init__ (self, name, health, attack_damage = 5, weapon="Fists", range=1, inventory = None, max_health = 100):
        if inventory is None:
            inventory = []

        #Input validation for string parameters
        self.str_input_checker(name)
        self.str_input_checker(weapon)
        for item in inventory:
            self.str_input_checker(item)
        #Input Validation for number parameters
        self.num_input_checker(health)
        self.num_input_checker(attack_damage)
        self.num_input_checker(range)
        self.num_input_checker(max_health)
        #set all values for the player object
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.weapon = weapon
        self.range = range
        self.inventory = inventory
        self.max_health = max_health

    #Getters and setters for all Player attributes
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self.str_input_checker(new_name)
        self._name = new_name

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        self.num_input_checker(new_health)
        self._health = new_health

    @property
    def attack_damage(self):
        return self._attack_damage
    
    @attack_damage.setter
    def attack_damage(self, new_attack_damage):
        self.num_input_checker(new_attack_damage)
        self._attack_damage = new_attack_damage

    @property
    def weapon(self):
        return self._weapon
    
    @weapon.setter
    def weapon(self, new_weapon):
        self.str_input_checker(new_weapon)
        self._weapon = new_weapon

    @property
    def range(self):
        return self._range
    
    @range.setter
    def range(self, new_range):
        self.num_input_checker(new_range)
        self._range = new_range

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, new_inventory):
        if not isinstance(new_inventory, list):
            raise TypeError("Inventory needs to be entered as a list")    
        for item in new_inventory:
            self.str_input_checker(item)

        self._inventory = new_inventory

    @property
    def max_health(self):
        return self._max_health
    
    @max_health.setter
    def max_health(self, new_max_health):
        self.num_input_checker(new_max_health)
        self._max_health = new_max_health

    def add_to_inventory(self, new_item):
        """adds a single item to the inventory
        Param: new_item is the string item to be added to the inventory list
        """
        self.str_input_checker(new_item)
        self._inventory.append(new_item)

    def attack(self):
        """Returns the player attack information
        """
        return ("Attack with: " + self.weapon + " for " + str(self.attack_damage) + " damage against creature within " + str(self.range) + " feet")

    def heal(self):
        """Heals player if they have a healing potion in their inventory with the amount they heal being maxed out at their max health
        if their health was below half before taking the potion and is above it after taking it then their damage is increased by 1.33(only from healing not setting health)
        """
        if "Healing Potion" in self.inventory:
            if self.health + 25 <= self.max_health:
                if self.health <= (self.max_health/2) and self.health + 25 > (self.max_health/2):
                    self.attack_damage = self.attack_damage * (4/3)
                self.health = self.health + 25
            else:
                self.health = self.max_health

    def take_damage(self, damage_amount):
        """Reduces player's health by the desired amount. If health goes below 0 the player dies and their inventory is emptied and if the player
        health is at or below half of their max health their damage output is reduced(only reduces when health is below half from damage not just setting)
        """
        self.num_input_checker(damage_amount)
        if self.health - damage_amount <= 0:
            self.inventory = []
        else:
            self.health = self.health - damage_amount
            if self.health <= (self.max_health/2):
                self.attack_damage = self.attack_damage * 0.75

    def output_to_file(self):
        """prints str for the player into a text file
        """
        with open("player_info.txt", "w") as file:
            file.write(str(self))

    def str_input_checker(self, test_string):
        """tests whether string input is valid(only contains characters, spaces, and/or numbers) and raises an error if it isn't
        Param: test_string is the string to be checked for validity
        Raises: ValueError if input is invalid
        """
        if (not isinstance(test_string, str) or not test_string.replace(" ", "").isalnum()):
                raise ValueError

    def num_input_checker(self, test_num):
        """tests whether num input is valid and raises an error if it isn't
        Param: test_num is the string to be checked for validity
        Raises: ValueError if input is invalid
        """
        if (not isinstance(test_num, (float, int)) or test_num < 0):
                raise ValueError

    def __str__(self):
        inventory_string = ", ".join(self._inventory)
        return ("TIMESTAMP: " + str(datetime.now().strftime("%Y:%D:%H:%M:%S")) + "\nName: " + self.name + "\nHealth: " + str(self.health) + "\nWeapon: " + self.weapon
                 + " Range: " + str(self.range) + " Damage: " + str(self.attack_damage) + "\nInventory items: " + inventory_string)