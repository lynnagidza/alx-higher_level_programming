#!/usr/bin/python3
"""Defines unittests for the max_integer function."""


import unittest
from max_integer import max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max_integer(self):
        """Test max_integer with a list of integers."""
        nums = [1, 5, 3, 9, 2]
        result = max_integer(nums)
        self.assertEqual(result, 9)

    def test_max_integer_negative_numbers(self):
        """Test max_integer with a list of negative numbers."""
        nums = [-5, -2, -9, -1, -3]
        result = max_integer(nums)
        self.assertEqual(result, -1)

    def test_max_integer_empty_list(self):
        """Test max_integer with an empty list."""
        nums = []
        result = max_integer(nums)
        self.assertIsNone(result)

    def test_max_integer_single_element(self):
        """Test max_integer with a list containing a single element."""
        nums = [42]
        result = max_integer(nums)
        self.assertEqual(result, 42)

    def test_max_integer_duplicate_values(self):
        """Test max_integer with a list containing duplicate values."""
        nums = [5, 2, 9, 5, 3, 9, 2]
        result = max_integer(nums)
        self.assertEqual(result, 9)

    def test_max_integer_mixed_types(self):
        """Test max_integer with a list containing mixed types."""
        nums = [1, 'a', 3, 5, 2]
        with self.assertRaises(TypeError):
            max_integer(nums)

    def test_max_integer_invalid_type(self):
        """Test max_integer with an invalid type for the list."""
        nums = 123
        with self.assertRaises(TypeError):
            max_integer(nums)


if __name__ == '__main__':
    unittest.main()
