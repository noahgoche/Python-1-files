"""
* Name         : Final Project Overview (Wizard)
* Author       : Noah Goche
* Created      : 8/3/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.132.1
* Description  : Derived class of player with overridden and additional methods
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from player import Player


class Wizard(Player):
    """
    Wizard derived player class
    """
    #Limited weapon options for a wizard character
    weapons = ["Wand", "Staff", "Orb"]
    def __init__ (self, name, health, attack_damage = 2, weapon="Wand", range=100, inventory = ["Spellbook", "Hat", "Potions"], max_health = 75,
                realm_name = "Canada", magic_type = "Light"):
        if weapon not in self.weapons:  
            raise ValueError    #Raise error if weapon is not in the set list
        super().__init__(name, health, attack_damage, weapon, range, inventory, max_health)
        self.str_input_checker(realm_name)
        self.str_input_checker(magic_type)
        self.realm_name = realm_name
        self.magic_type = magic_type

    @property
    def realm_name(self):
        return self._realm_name
            
    @realm_name.setter
    def realm_name(self, new_realm_name):
        self.str_input_checker(new_realm_name)
        self._realm_name = new_realm_name

    @property
    def magic_type(self):
        return self._magic_type
            
    @magic_type.setter
    def magic_type(self, new_magic_type):
        self.str_input_checker(new_magic_type)
        self._magic_type = new_magic_type
    

    def heal(self):
        """Heals player for 50 health without needing a potion
        """
        if self.health + 50 <= self.max_health:
            self.health = self.health + 50
        else:
            self.health = self.max_health

    def take_damage(self, damage_amount):
        """Reduces player's health by the desired amount. If health goes below 0 the player dies and their inventory is emptied unless they have a spellbook otherwise it 
        only clears the spellbook from the inventory
        """
        self.num_input_checker(damage_amount)
        if self.health - damage_amount <= 0:
            if not "Spellbook" in self.inventory:
                self.inventory = []
        else:
            self.health = self.health - damage_amount

    def __str__(self):
        return super().__str__() + "\nRealm: " + self.realm_name + "\nPractices " + self.magic_type + " magic"