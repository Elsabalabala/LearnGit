#!usr/bin/env python
#coding=utf-8

import nwmath
import unittest

class AddTest(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = nwmath.add(1, 2)
        self.assertEqual(result, 3)

class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the mymath library
    """
    def test_subtract_integers(self):
        """
        Test that subtracting integers returns the correct result
        """
        result = nwmath.subtract(10, 8)
        self.assertEqual(result, 2)

if __name__ == '__main__':
        unittest.main()
