"""
SAMPLE TESTS
"""

from django.test import SimpleTestCase

from app import calc 

class CalcTests(SimpleTestCase):
    """TEST THE CALC MODULE"""
    
    def test_add_numbers(self):
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
        
    def test_divide_numbers(self):
        res = calc.divide(10, 5)
        
        self.assertEqual(res, 2)