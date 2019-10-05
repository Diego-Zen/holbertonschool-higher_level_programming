#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_none(self):
        self.assertIsNone(max_integer())

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 2, 3, 1, 8, 6, 3]), 8)

    def test_diff(self):
        self.assertNotEqual(max_integer([1, 4, 5, 1]), 3)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, [1, "3", 2])


if __name__ == '__main__':
    unittest.main()
