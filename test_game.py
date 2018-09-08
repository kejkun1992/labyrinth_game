# -*- coding: utf-8 -*-

import unittest
import game


class TestTurnLabyrinth(unittest.TestCase):    
    def test_turn_left(self):
        self.labyrinths = game.Labyrinths()
        
        self.lab = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.result = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]
        
        self.assertEqual(self.labyrinths.turn_left(self.lab), self.result)
        
    def test_turn_left2(self):
        self.labyrinths = game.Labyrinths()
        
        self.lab = [[1,1,2,1,1],[1,0,1,1,1],[0,1,0,1,0],[1,1,1,0,0],
                     [1,1,1,1,1],[2,2,0,1,0]]
        self.result = [[1,1,0,0,1,0],[1,1,1,0,1,1],[2,1,0,1,1,0],
                        [1,0,1,1,1,2],[1,1,0,1,1,2]]
        
        self.assertEqual(self.labyrinths.turn_left(self.lab), self.result)
        
    def test_turn_right(self):
        self.labyrinths = game.Labyrinths()
        
        self.lab = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.result = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
        
        self.assertEqual(self.labyrinths.turn_right(self.lab), self.result)
        
    def test_turn_right2(self):
        self.labyrinths = game.Labyrinths()
        
        self.lab = [[1,1,2,1,1],[1,0,1,1,1],[0,1,0,1,0],[1,1,1,0,0],
                     [1,1,1,1,1],[2,2,0,1,0]]
        self.result = [[2,1,1,0,1,1],[2,1,1,1,0,1],[0,1,1,0,1,2],
                        [1,1,0,1,1,1],[0,1,0,0,1,1]]
        
        self.assertEqual(self.labyrinths.turn_right(self.lab), self.result)
    
    def test_turn_around(self):
        self.labyrinths = game.Labyrinths()
        
        self.lab = [[1,1,2,1,1],[1,0,1,1,1],[0,1,0,1,0],[1,1,1,0,0],
                     [1,1,1,1,1],[2,2,0,1,0]]
        self.result = [[0,1,0,2,2],[1,1,1,1,1],[0,0,1,1,1],
                        [0,1,0,1,0],[1,1,1,0,1],[1,1,2,1,1]]
        
        self.assertEqual(self.labyrinths.turn_around(self.lab), self.result)
        
if __name__ == '__main__':
    unittest.main()