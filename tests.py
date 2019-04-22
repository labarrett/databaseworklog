import unittest
from unittest import TestCase, mock

import datetime

import worklog

class EntryTests(unittest.TestCase):

    def test_get_date(self):
        answer1 = worklog.get_date()
        self.assertIsInstance(answer1, str)

if __name__ == '__main__':
    unittest.main()
