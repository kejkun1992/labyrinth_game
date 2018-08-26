# -*- coding: utf-8 -*-

import unittest
import game


class TestTurnLabyrinth(unittest.TestCase):    
    def test_turn_left(self):
        self.labyrinths = game.Labyrinths()
        self.assertEqual(self.labyrinths.turn_left('a'), 'a')
    
if __name__ == '__main__':
    unittest.main()