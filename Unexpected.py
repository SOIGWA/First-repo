# MATH TESTING
import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):
    def test_sqrt(self):
        result = get_sqrt(144)
        expected_result = 12
        self.assertEqual(result, expected_result)

       
        with self.assertRaises(TypeError):
            _ = 'Twelve' in 12

    def test_divide(self):
        result = divide(144, 12)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()

