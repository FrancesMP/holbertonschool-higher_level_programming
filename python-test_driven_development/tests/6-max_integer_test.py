#!/usr/bin/python3

"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    # Check if element in list are int
    def test_type(self):
        test_list = [1, 2, 3, 4]
        for element in test_list:
            self.assertIsInstance(element, int)

    # Check max value
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 42, 4]), 42)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([42]), 42)

    # Check empty list
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
