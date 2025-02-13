
"""
Unit tests for the Water Pitchers Problem using A* search algorithm.
"""

__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"
__email__ = "javid.alakbarli@gwmail.gwu.edu"

import unittest
from utils import h_of_n, f_of_n, read_input
from main import a_star_pitchers
import os

class TestWaterPitchers(unittest.TestCase):
    def setUp(self):
        with open('input.txt', 'w') as f:
            f.write('2,3,5\n10')
        
    def tearDown(self):
        if os.path.exists('input.txt'):
            os.remove('input.txt')

    def test_read_input(self):
        pitchers, target = read_input()
        self.assertEqual(pitchers[:-1], [2, 3, 5])
        self.assertEqual(pitchers[-1], float('inf'))  
        self.assertEqual(target, 10)

    def test_h_function(self):
        state = (0, 0, 0, 0)  
        target = 10
        pitchers_capacity = [1, 2, 3, float('inf')]
        h = h_of_n(state, target, pitchers_capacity)
        self.assertTrue(h >= 0)

    def test_f_function(self):
        g = 5
        h = 3
        f = f_of_n(g, h)
        self.assertEqual(f, 8)

    def test_solve_water_pitchers_solvable(self):
        with open('input.txt', 'w') as f:
            f.write('2,3,5\n4')
        result = a_star_pitchers()
        self.assertGreater(result, 0)

    def test_solve_water_pitchers_unsolvable(self):
        with open('input.txt', 'w') as f:
            f.write('2,4,6\n3')
        result = a_star_pitchers()
        self.assertEqual(result, -1)

    def test_solve_water_pitchers_zero_steps(self):
        with open('input.txt', 'w') as f:
            f.write('2,3,5\n0')
        result = a_star_pitchers()
        self.assertEqual(result, 0)

    def test_solve_water_pitchers_direct_fill(self):
        with open('input.txt', 'w') as f:
            f.write('2,3,5\n5')
        result = a_star_pitchers()
        self.assertEqual(result, 2)  

if __name__ == '__main__':
    unittest.main()