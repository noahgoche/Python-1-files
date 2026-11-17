"""
* Name         : Final Project Overview (Player unit tests)
* Author       : Noah Goche
* Created      : 8/3/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.132.1
* Description  : Unit tests for player class
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import unittest
from datetime import datetime
from player import Player

class TestPlayers(unittest.TestCase):

    def setUp(self):
        self.player = Player("Noah Goche", 100, 10, "Sword", 2, ["Healing Potion", "Map", "Food"], 125)

    def tearDown(self):
        del self.player

    #Test input validation methods. If these pass then all the times they're used for input are good eliminating extra tests
    #Test valid string
    def test_str_input_checker(self):
        self.player.str_input_checker("Test Name1") #Numbers are allowed as gamertags often have them

    #Test invalid string
    def test_str_input_checker_invalid_input(self):
        with self.assertRaises(ValueError):
            self.player.str_input_checker("Test Name2!") #Symbols aren't allowed
        
    #Test empty string
    def test_str_input_checker_empty(self):
        with self.assertRaises(ValueError):
            self.player.str_input_checker("") 

    #Test valid numbers (decimal or integers are acceptable)
    def test_num_input_checker(self):
        self.player.num_input_checker(50)

    #Test valid zero as edge case
    def test_num_input_checker_zero(self):
        self.player.num_input_checker(0)

    #Test invalid(less than zero) numbers
    def test_num_input_checker_invalid(self):
        with self.assertRaises(ValueError):
            self.player.num_input_checker(-1)

    #Test invalid(string input) as a non number input
    def test_num_input_checker_non_number(self):
        with self.assertRaises(ValueError):
            self.player.num_input_checker("hello")

    #Test for empty value in num input checker
    def test_num_input_checker_empty(self):
        with self.assertRaises(ValueError):
            self.player.num_input_checker(None)

    #Test player with necessary and default values
    def test_with_default_values(self):
        new_player = Player("John Doe", 100)
        self.assertEqual(new_player.name, "John Doe")
        self.assertAlmostEqual(new_player.health, 100)  #almost equal in case health is a decimal value
        self.assertAlmostEqual(new_player.attack_damage, 5)  #almost equal in case attack damage is a decimal value
        self.assertEqual(new_player.weapon, "Fists")
        self.assertAlmostEqual(new_player.range, 1)  #almost equal in case range is a decimal value
        self.assertEqual(new_player.inventory, [])
        self.assertAlmostEqual(new_player.max_health, 100) #almost equal in case max health is a decimal value

    #Test with setup values
    def test_with_set_values(self):
        self.assertEqual(self.player.name, "Noah Goche")
        self.assertAlmostEqual(self.player.health, 100)
        self.assertAlmostEqual(self.player.attack_damage, 10)
        self.assertEqual(self.player.weapon, "Sword")
        self.assertAlmostEqual(self.player.range, 2)
        self.assertEqual(self.player.inventory, ["Healing Potion", "Map", "Food"])
        self.assertAlmostEqual(self.player.max_health, 125)

    #Test creation raises errors using input checker method for strings
    def test_create_bad_string(self):
        with self.assertRaises(ValueError):
            player = Player(432, 4)

    #Test creation raises errors using input checker method for numbers
    def test_create_bad_number(self):
        with self.assertRaises(ValueError):
            player = Player("Test name3", -44)

    #Test adding items to the player's inventory
    def test_adding_to_inventory(self):
        self.player.add_to_inventory("Shield")
        self.assertIn("Shield", self.player.inventory)

    #Test for attack output
    def test_attack(self):
        expected_attack_output = "Attack with: Sword for 10 damage against creature within 2 feet"
        self.assertEqual(self.player.attack(), expected_attack_output)

    #Test for healing 
    def test_heal(self):
        self.player.health = 50     #set to less than the max health of 125
        self.player.heal()
        self.assertAlmostEqual(self.player.health, 75)

    #Test without healing potion
    def test_heal_no_potion(self):
        self.player.health = 75 #set to less than the max health of 125
        self.player.inventory = []  #clear inventory of healing potions
        self.player.heal()
        self.assertAlmostEqual(self.player.health, 75)  #Health should remain 75 as there was no healing potion

    #Test to make sure max health isn't exceded
    def test_heal_max_health(self):
        self.player.health = 125  #set to the max health of 125
        self.player.heal()
        self.assertAlmostEqual(self.player.health, 125)
        
    #Test damage is increased from healing
    def test_dmg_boost(self):
        self.player.health = 62.5
        self.player.heal()
        boosted_dmg = (10*(4/3))
        self.assertAlmostEqual(self.player.attack_damage, boosted_dmg)

    #Test taking damage 
    def test_take_dmg(self):
        self.player.take_damage(10)
        self.assertAlmostEqual(self.player.health, 90)

    #Test taking damage and lowering attack dmg 
    def test_lower_attack_dmg(self):
        self.player.take_damage(50)
        lower_dmg = (10 * (3/4))
        self.assertAlmostEqual(self.player.attack_damage, lower_dmg)

    #Test inventory is emptied when health is at zero or below
    def test_take_fatal_dmg(self):
        self.player.take_damage(120)
        self.assertEqual(self.player.inventory, [])

    #Test string output matches expected result
    def test_str_output(self):
        str_output = str(self.player)
        str_expected_no_timestamp = "Name: Noah Goche\nHealth: 100\nWeapon: Sword Range: 2 Damage: 10\nInventory items: Healing Potion, Map, Food" 
        self.assertIn(str_expected_no_timestamp, str_output)    #Tests without the datetime.now


if __name__ == '__main__':
    unittest.main()
