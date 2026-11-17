"""
* Name         : Final Project Overview (Warrior player derived class)
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

class Warrior(Player):
    """
    Warrior derived player class
    """
    #Limited weapon options for a warrior character
    weapons = ["Axe", "Sword", "Spear", "Knife"]
    def __init__ (self, name, health, attack_damage = 7, weapon="Axe", range=2, inventory = ["Healing Potion", "Shield"], max_health = 125, kingdom_name = "Iowa"):
        if weapon not in self.weapons:  
            raise ValueError    #Raise error if weapon is not in the set list
        super().__init__(name, health, attack_damage, weapon, range, inventory, max_health)
        self.str_input_checker(kingdom_name)
        self.kingdom_name = kingdom_name

    @property
    def kingdom_name(self):
        return self._kingdom_name
        
    @kingdom_name.setter
    def kingdom_name(self, new_kingdom_name):
        self.str_input_checker(new_kingdom_name)
        self._kingdom_name = new_kingdom_name

    def heal(self):
        """Heals player if they have a healing potion in their inventory with the amount they heal being maxed out at their max health. Healing
        is stronger for a warrior and raising above half health doesn't increase warrior health
        """
        if "Healing Potion" in self.inventory:
            if self.health + 40 <= self.max_health:
                self.health = self.health + 40
            else:
                self.health = self.max_health

    def take_damage(self, damage_amount):
        """Reduces player's health by the desired amount. If health goes below 0 the player dies and their inventory is emptied. Attack damage 
        doesn't get reduced for a warrior
        """
        self.num_input_checker(damage_amount)
        if self.health - damage_amount <= 0:
            self.inventory = []
        else:
            self.health = self.health - damage_amount

    def __str__(self):
        return super().__str__() + "\nKingdom: " + self.kingdom_name