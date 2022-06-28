#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defining unittest class"""
    def test_ordered_list(self):
        """Testing ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Testing unordered list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Testing empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Testing single element"""
        self.assertEqual(max_integer([1]), 1)

    def test_negative_list(self):
        """Testing negative list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_list(self):
        """Testing float list"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)


if __name__ == '__main__':
    unittest.main()
