import unittest
from suminput_001 import suminput

class codingTestWhitPythonTest(unittest.TestCase):
    def test_suminput(self):
        # Test with valid input
        input_count = 5
        input_list = '12345'
        expected_output_str = 15
        self.assertEqual(suminput(input_count, input_list), expected_output_str)

        # Test with all zeros
        input_count = 1
        input_list = '1'
        expected_output_str = 1
        self.assertEqual(suminput(input_count, input_list), expected_output_str)

        # Test with all ones
        input_count = 25
        input_list = '7000000000000000000000000'
        expected_output_str = 7
        self.assertEqual(suminput(input_count, input_list), expected_output_str)

        # Test with empty list
        input_count = 11
        input_list = '10987654321'
        expected_output_str = 46
        self.assertEqual(suminput(input_count, input_list), expected_output_str)

if __name__ == '__main__':
    unittest.main()