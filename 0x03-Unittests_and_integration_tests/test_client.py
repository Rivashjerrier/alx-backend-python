#!/usr/bin/env python3
"""
test_client.py module
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient(unittest.TestCase) class and implementation
    of the test_org method
    """
    @parameterized.expand([
        ('google', {"login": "google"}),
        ('abc', {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org, mocked, result):
        """
        This method tests that GithubOrgClient.org returns the correct value
        """
        mocked.return_value = result
        test_client = GithubOrgClient(org)
        test_org = test_client.org()
        self.assertEqual(test_org, result)


if __name__ == '__main__':
    unittest.main()
