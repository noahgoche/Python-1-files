"""
* Name         : Final Project Overview (Warrior unit tests)
* Author       : Noah Goche
* Created      : 8/3/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.132.1
* Description  : Unit tests for warrior class
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import unittest
from datetime import datetime
from warrior import Warrior

class TestWarriors(unittest.TestCase):
    def setUp(self):
        self.warrior = Warrior("Bill Nye", 300, 8, "Spear", 4, ["Healing Potion", "Lab Coat"], 360, "Science")

    def tearDown(self):
        del self.warrior

    #Test the default attributes warrior
    def test_default_warrior(self):
        new_warrior = Warrior("John Warrior", 100)
        self.assertEqual(new_warrior.name, "John Warrior")
        self.assertAlmostEqual(new_warrior.health, 100)
        self.assertAlmostEqual(new_warrior.attack_damage, 7)
        self.assertEqual(new_warrior.weapon, "Axe")
        self.assertAlmostEqual(new_warrior.range, 2)
        self.assertEqual(new_warrior.inventory, ["Healing Potion", "Shield"])
        self.assertAlmostEqual(new_warrior.max_health, 125)
        self.assertEqual(new_warrior.kingdom_name, "Iowa")

    #Test with setup values
    def test_warrior_set_values(self):
        self.assertEqual(self.warrior.name, "Bill Nye")
        self.assertAlmostEqual(self.warrior.health, 300)
        self.assertAlmostEqual(self.warrior.attack_damage, 8)
        self.assertEqual(self.warrior.weapon, "Spear")
        self.assertAlmostEqual(self.warrior.range, 4)
        self.assertEqual(self.warrior.inventory, ["Healing Potion", "Lab Coat"])
        self.assertAlmostEqual(self.warrior.max_health, 360)
        self.assertEqual(self.warrior.kingdom_name, "Science")       

    #Test with invalid weapon
    def test_invalid_weapon(self):
        with self.assertRaises(ValueError):
            new_warrior = Warrior("John", 100, 4, "Nunchucks")

    #Test health changes by 40 not 25 for a warrior
    def test_warrior_healing(self):
        self.warrior.health = 100
        self.warrior.heal()
        self.assertAlmostEqual(self.warrior.health, 140)

    #Test health still doesn't increase beyond max health
    def test_heal_to_max(self):
        self.warrior.health = 355
        self.warrior.heal()
        self.assertAlmostEqual(self.warrior.health, 360)
 
    #Test inventory empties with 0 or lower health
    def test_lose_inventory_on_death(self):
        self.warrior.health = 10
        self.warrior.take_damage(10)
        self.assertEqual(self.warrior.inventory, [])

    #Test string output
    def test_str_warrior_out(self):
        str_output = str(self.warrior)
        str_expected_no_timestamp = "Name: Bill Nye\nHealth: 300\nWeapon: Spear Range: 4 Damage: 8\nInventory items: Healing Potion, Lab Coat\nKingdom: Science" 
        self.assertIn(str_expected_no_timestamp, str_output)    #Tests without the datetime.now


if __name__ == "__main__":
    unittest.main()