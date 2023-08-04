#!/usr/bin/env python3
"""
test_client.py module
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient(unittest.TestCase) class and implementation
    of the test_org method
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_function):
        """
        This method tests that GithubOrgClient.org returns the correct value
        """
        mock_function.return_value = {"login": org}
        test_client = GithubOrgClient(org)
        test_org = test_client.org()
        self.assertEqual(test_org, {"login": org})

    def test_public_repos_url(self):
        """
        test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url
        """
        known_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        with patch.object(GithubOrgClient, 'org', return_value=known_payload):
            test_client = GithubOrgClient("google")
            public_repos_url = test_client._public_repos_url
            res = "https://api.github.com/orgs/google/repos"
            self.assertEqual(public_repos_url, res)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license, result):
        """
        Test the has_license method
        """
        test_client = GithubOrgClient('google')
        client_result = test_client.has_license(repo, license)
        self.assertEqual(client_result, result)
