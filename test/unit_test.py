import unittest
import datetime
from app.details import *
from app.utils import *

class UnitTest(unittest.TestCase):
    def test_find_week(self):
        self.assertEqual(find_week('16.11.2020'), datetime.datetime(2020, 11, 16, 0, 0))
        self.assertEqual(find_week('15.11.2020'), datetime.datetime(2020, 11, 9, 0, 0))
        self.assertEqual(find_week('26.11.2020'), datetime.datetime(2020, 11, 23, 0, 0))
        self.assertEqual(find_week('15.10.2020'), datetime.datetime(2020, 10, 12, 0, 0))
        self.assertEqual(find_week('29.11.2020'), datetime.datetime(2020, 11, 23, 0, 0))
        self.assertRaises(ValueError, find_week, '31.11.2020')
        self.assertRaises(ValueError, find_week, 'date')
    
    
    def test_checkDate(self):
        self.assertEqual(checkDate('2020-09-11'), 'Invalid date')
        
        today = date.today()
        next_year = '05.04.' + str(today.year + 1)
        self.assertEqual(checkDate(next_year), next_year)
        
        cur_year = '01.09.' + str(today.year)
        self.assertEqual(checkDate(cur_year), cur_year)
        
        next_year = '31.07.' + str(today.year + 1)
        self.assertEqual(checkDate(next_year), 'Incorrect Date')
        
        last_year = '05.10.' + str(today.year - 1)
        self.assertEqual(checkDate(last_year), 'Incorrect Date')
     
     
    def test_checkGroup(self):
        self.assertEqual(checkGroup('3530904/80105'), '3530904/80105')
        self.assertFalse(checkGroup('3530904_80105'))
        self.assertFalse(checkGroup('3530904/0105'))
        self.assertFalse(checkGroup('353090/80105'))
        self.assertFalse(checkGroup('g530904/80105'))
        self.assertFalse(checkGroup('3530904/8010g'))
     
     
if __name__ == '__main__':
    unittest.main()