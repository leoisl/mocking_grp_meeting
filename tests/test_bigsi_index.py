import unittest
from unittest.mock import Mock, patch
from src.index.implementation.bigsi_index import BigsiIndex

class Test_BigsiIndex_search(unittest.TestCase):
    @patch("requests.get")
    def test_dummy_json(self, requests_get_mock):
        response_mock = Mock()
        response_mock.json.return_value = "dummy_json"
        requests_get_mock.return_value = response_mock

        bigsi_index = BigsiIndex("dont_matter")

        actual = bigsi_index._search("ACGT")
        expected = "dummy_json"

        self.assertEqual(actual, expected)
