import unittest
from unittest import TestCase, mock
from unittest.mock import patch

import datetime
from peewee import SqliteDatabase
import worklog

MODELS = [worklog.Entry]

test_db = SqliteDatabase(':memory:')

class EntryTests(unittest.TestCase):
    def setUp(self):
          test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
          test_db.connect
          test_db.create_tables(MODELS)
  

    def test_get_date(self):
        to_pass_in = ['12/13/14']

        with patch('builtins.input', side_effect=to_pass_in):
            with patch('builtins.print', side_effect=print) as mock:
                result = worklog.get_date()
                self.assertIsInstance(result, str)

    def test_date_invalid(self):

        to_pass_in = ['22/13/14', '12/13/14']

        with patch('builtins.input', side_effect=to_pass_in):
            with patch('builtins.print', side_effect=print) as mock:
                result = worklog.get_date()
                mock.assert_called_once_with("Opps! Wrong date format. Please post in MM/DD/YY format ")
        
       
    def test_add_entries(self):
    
      to_pass_in = ['Lindsay', 'Task 1', '12/13/14', '00:45', 'no notes', 'Y', 'q']
      
      with patch('builtins.input', side_effect=to_pass_in):
            result = worklog.add_entry()
            self.assertIsNotNone(result)


    def test_search_menu(self):
    
      to_pass_in = ['a','Lindsay', 'Task 1', '12/13/14', '00:45', 'no notes', 'Y', 'q']
      
      with patch('builtins.input', side_effect=to_pass_in):
              result = worklog.menu_loop()
              self.assertIsNotNone(result)
              
              
if __name__ == '__main__':
    unittest.main()
