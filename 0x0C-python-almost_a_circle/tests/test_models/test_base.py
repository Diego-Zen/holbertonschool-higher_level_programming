#!/usr/bin/python3
"""
    Unit test base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test base
    """

    def test_none(self):
        """test id"""
        self.assertEqual(Base(12), 12)


if __name__ == '__main__':
    unittedt.main()
