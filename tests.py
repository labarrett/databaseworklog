import unittest
from unittest import TestCase, mock
from unittest.mock import patch

import datetime

import worklog

class EntryTests(unittest.TestCase):

    def test_get_date(self):
        answer1 = worklog.get_date()
        self.assertIsInstance(answer1, str)

    def test_date_invalid(self):

        to_pass_in = ['22/13/14', '12/13/14']

        with patch('builtins.input', side_effect=to_pass_in):
            with patch('builtins.print', side_effect=print) as mock:
                result = worklog.get_date()
                mock.assert_called_once_with("Opps! Wrong date format. Please post in MM/DD/YY format ")
        

if __name__ == '__main__':
    unittest.main()
