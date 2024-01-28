#!/usr/bin/python3
"""
Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_sorted_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_float_list(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

if __name__ == '__main__':
    unittest.main()
