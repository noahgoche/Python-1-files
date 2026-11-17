"""
* Name         : Final Project Overview (Wizard unit tests)
* Author       : Noah Goche
* Created      : 8/3/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.132.1
* Description  : Unit tests for wizard class
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import unittest
from datetime import datetime
from wizard import Wizard

class TestWizards(unittest.TestCase):
    def setUp(self):
        self.wizard = Wizard("Noah Wizard", 55, 3.3, "Orb", 40, ["Spellbook", "Potions"], 65, "Beyonder Realm", "Dark")

    def tearDown(self):
        del self.wizard

    #Test the default attributes wizard
    def test_default_wizard(self):
        new_wizard = Wizard("Harry Potter", 45)
        self.assertEqual(new_wizard.name, "Harry Potter")
        self.assertAlmostEqual(new_wizard.health, 45)
        self.assertAlmostEqual(new_wizard.attack_damage, 2)
        self.assertEqual(new_wizard.weapon, "Wand")
        self.assertAlmostEqual(new_wizard.range, 100)
        self.assertEqual(new_wizard.inventory, ["Spellbook", "Hat", "Potions"])
        self.assertAlmostEqual(new_wizard.max_health, 75)
        self.assertEqual(new_wizard.realm_name, "Canada")
        self.assertEqual(new_wizard.magic_type, "Light")

    #Test with setup values
    def test_wizard_set_values(self):
        self.assertEqual(self.wizard.name, "Noah Wizard")
        self.assertAlmostEqual(self.wizard.health, 55)
        self.assertAlmostEqual(self.wizard.attack_damage, 3.3)
        self.assertEqual(self.wizard.weapon, "Orb")
        self.assertAlmostEqual(self.wizard.range, 40)
        self.assertEqual(self.wizard.inventory, ["Spellbook", "Potions"])
        self.assertAlmostEqual(self.wizard.max_health, 65)
        self.assertEqual(self.wizard.realm_name, "Beyonder Realm")
        self.assertEqual(self.wizard.magic_type, "Dark")          

    #Test with invalid weapon
    def test_invalid_weapon(self):
        with self.assertRaises(ValueError):
            new_wizard = Wizard("Kevin", 22, 2, "Nunchucks")    

    #Test health changes by 50 not 25 for a wizard
    def test_wizard_healing(self):
        self.wizard.health = 10
        self.wizard.heal()
        self.assertAlmostEqual(self.wizard.health, 60)

    #Test health still doesn't increase beyond max health
    def test_heal_to_max(self):
        self.wizard.health = 20
        self.wizard.heal()
        self.assertAlmostEqual(self.wizard.health, 65)

    #Test inventory doesn't empty upon death with Spellbook
    def test_death_keeps_inventory(self):
        self.wizard.inventory = ["Spellbook", "Hat"]
        self.wizard.health = 10
        self.wizard.take_damage(15)
        self.assertEqual(self.wizard.inventory, ["Spellbook", "Hat"])

    #Test inventory doesn't empty upon death with Spellbook
    def test_death_drops_inventory(self):
        self.wizard.inventory = ["Spare wand", "Hat"]
        self.wizard.health = 10
        self.wizard.take_damage(15)
        self.assertEqual(self.wizard.inventory, [])

    #Test taking damage
    def test_take_damage(self):
        self.wizard.health = 30
        self.wizard.take_damage(15)
        self.assertAlmostEqual(self.wizard.health, 15)

    #Test str for wizard
    def test_str_warrior_out(self):
        str_output = str(self.wizard)
        str_expected_no_timestamp = "Name: Noah Wizard\nHealth: 55\nWeapon: Orb Range: 40 Damage: 3.3\nInventory items: Spellbook,"
        "Potions\nRealm: Beyonder Realm\nPractices Dark magic" 
        self.assertIn(str_expected_no_timestamp, str_output)    #Tests without the datetime.now
    
if __name__ == "__main__":
    unittest.main()