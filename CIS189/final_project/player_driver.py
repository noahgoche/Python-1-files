"""
* Name         : Final Project Overview (Driver class)
* Author       : Noah Goche
* Created      : 8/3/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.132.1
* Description  : Driver class to use the player and derived classes
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

from player import Player
from warrior import Warrior
from wizard import Wizard

def main():
    base_player_dict = {"name": "Noah Goche", "health": 100, "attack_damage": 10, "weapon": "Sword", "range": 2, "inventory": ["Healing Potion","Map", "Food"],
          "max_health": 125} #creates a base player
    warrior_player_dict = {"name": "Bill Goche", "health": 200, "attack_damage": 10, "weapon": "Spear", "range": 4, "inventory": ["Healing Potion", "Map", "Food"],
          "max_health": 200, "kingdom_name": "England"} #Creates warrior player
    wizard_player_dict = {"name": "Gandalf Gray", "health": 50, "attack_damage": 4, "weapon": "Staff", "range": 50, "inventory":["Spellbook"],"max_health": 200,
          "realm_name": "LOTR", "magic_type": "Light"}
    
    players_dict = {"Base player": Player(**base_player_dict),
                    "Warrior player": Warrior(**warrior_player_dict),
                    "Wizard player": Wizard(**wizard_player_dict)}

    print("Create a warrior character")
    name = input("Enter name: ")
    health = input("Enter health: ")
    attack_damage = input("Enter attack_damage: ")
    weapon = input("Enter a weapon: ")
    range = input("Enter range: ")
    inventory = input("Enter inventory items separated by a comma: ").strip()
    inventory_list = [item for item in inventory.split(',')]
    max_health = input("Enter max health: ")
    kingdom = input("Enter a kingdom: ")
    input_warrior = Warrior(name, float(health), float(attack_damage), weapon, float(range), inventory_list, float(max_health), kingdom)
    players_dict["New Warrior"] = input_warrior

    print("\n")
    for player, player_info in players_dict.items():
        print(f"{player}\n{player_info}\n")

    input_warrior.output_to_file()


if __name__ == '__main__':
    main()
