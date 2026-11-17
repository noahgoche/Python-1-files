"""
* Name         : M13 T1: GUI Assignment(unit tests)
* Author       : Noah Goche
* Created      : 7/29/2026
* Course       : CIS189 30546
* IDE          : Visual Studio Code Version 1.129.1
* Description  : Class creates a game that has a gui with buttons from 1 to max, a value given by the user, and the user must click buttons
to guess the value
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""

import unittest
from number_guesser import NumberGuesser

class NumberGuesserTest(unittest.TestCase):

    def setUp(self):
        self.number_game = NumberGuesser(10)    #creates game with max = 10

    def tearDown(self):
        del self.number_game

    def test_initial_attributes(self):
        self.assertEqual(self.number_game.max, 10)

    def test_add_to_guessed_list(self):
        self.number_game.add_guess(2)
        self.number_game.add_guess(3)
        self.assertEqual(self.number_game.guessed_list, [2, 3])

if __name__ == '__main__':
    unittest.main()
