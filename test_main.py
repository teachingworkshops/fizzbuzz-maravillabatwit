import unittest
from main import calculate_response

class TestFizzBuzz(unittest.TestCase):

    def test_calculate_response(self):
        self.assertEqual(calculate_response(-99), "-99")
        self.assertEqual(calculate_response(-1), "-1")
        self.assertEqual(calculate_response(0), "0")
        self.assertEqual(calculate_response(1), "1")
        self.assertEqual(calculate_response(2), "2")
        self.assertEqual(calculate_response(3), "fizz")
        self.assertEqual(calculate_response(4), "4")
        self.assertEqual(calculate_response(5), "buzz")
        self.assertEqual(calculate_response(6), "fizz")
        self.assertEqual(calculate_response(7), "7")
        self.assertEqual(calculate_response(9), "fizz")
        self.assertEqual(calculate_response(10), "buzz")
        self.assertEqual(calculate_response(11), "11")
        self.assertEqual(calculate_response(14), "14")
        self.assertEqual(calculate_response(15), "fizzbuzz")
        self.assertEqual(calculate_response(16), "16")
        self.assertEqual(calculate_response(29), "29")
        self.assertEqual(calculate_response(30), "fizzbuzz")

if __name__ == '__main__':
    unittest.main()
