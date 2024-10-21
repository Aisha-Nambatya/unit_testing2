import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    
    def test_factorial(self):

        test_cases = {
            0: 1,   # 0! = 1
            1: 1,   # 1! = 1
            2: 2,   # 2! = 2
            3: 6,   # 3! = 6
            4: 24,  # 4! = 24
            5: 120  # 5! = 120
        }
        
        for n, expected in test_cases.items():
            self.assertEqual(factorial(n), expected)

    def test_factorial_negative(self):

        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
