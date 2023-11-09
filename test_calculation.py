import unittest
import pytest
import calculation

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculation.add(10, 5), 15)
        self.assertEqual(calculation.add(7, 5), 12)
        self.assertEqual(calculation.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculation.subtract(10, 5), 5)
        self.assertEqual(calculation.subtract(7, 5), 2)
        self.assertEqual(calculation.subtract(-1, -1), 0)


        
        
        

