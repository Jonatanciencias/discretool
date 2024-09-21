# tests/test_common_tools.py
import unittest
from src.common_tools import gcd, lcm, generate_primes

class TestCommonTools(unittest.TestCase):
    
    def test_gcd(self):
        self.assertEqual(gcd(60, 48), 12)
    
    def test_lcm(self):
        self.assertEqual(lcm(15, 20), 60)
    
    def test_generate_primes(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()
