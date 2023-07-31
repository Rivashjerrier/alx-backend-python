#!/usr/bin/env python3
""" test_utils.py module """

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class that inherits from unittest.TestCase """

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ TestAccessNestedMap.test_access_nested_map method to test
            that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
