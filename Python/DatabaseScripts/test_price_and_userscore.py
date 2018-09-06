import unittest
from price_and_userscore import get_data


class TestPriceAndUserscore(unittest.TestCase):

    def test_get_data(self):
        appid_correct = 730
        appid_incorrect = 869
        self.assertEqual(get_data(appid_correct), (88, 1499))
        self.assertEqual(get_data(appid_incorrect), (0, None))