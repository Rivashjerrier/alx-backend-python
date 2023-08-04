#!/usr/bin/env python3
""" test_utils.py module """

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Uses the assertRaises context manager to test that
            a KeyError is raised correctly
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ TestGetJson.test_get_json method to test that utils.get_json
        returns the expected result
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Tests that the mocked get method was called exactly once
            with test_url as argument.
            Test that the output of get_json is equal to test_payload.
        """
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload
        res = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test class for the memoize function """

    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result
            is returned but a_method is only called once using
            assert_called_once
        """

        class TestClass:
            """ TestClass that was provided """
            def a_method(self):
                """ method return value """
                return 42

            @memoize
            def a_property(self):
                """ property returns value """
                return self.a_method()

            test_instance = TestClass()
            with patch.object(test_instance, "a_method") as mock_a_method:
                test_instance.a_property()
                test_instance.a_property()
                mock_a_method.assert_called_once()
