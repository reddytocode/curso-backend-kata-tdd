from unittest import TestCase
import unittest
from string_calculator import StringCalculator


class StringCalculatorTest(TestCase):
    def setUp(self):
        self.string_calculator = StringCalculator()

    def test_string_calculator_empty_string_as_input(self):
        input_test_string = ''
        expected_number_response = 0
        response_number = self.string_calculator.add(input_test_string)
        self.assertEqual(response_number, expected_number_response)
    
    def test_string_calculator_one_value(self):
        input_test_string = '3'
        expected_number_response = 3
        response_number = self.string_calculator.add(input_test_string)
        self.assertEqual(response_number, expected_number_response)

    def test_string_calculator_two_values_delimited(self):
        input_test_string = '10,20'
        expected_number_response = 30
        response_number = self.string_calculator.add(input_test_string)
        self.assertEqual(response_number, expected_number_response)

    def test_string_calculator_two_lines_values(self):
        input_test_string = '1\n2'
        expected_number_response = 3
        response_number = self.string_calculator.add(input_test_string)
        self.assertEqual(response_number, expected_number_response)

    def test_string_calculator_two_lines_values_delimited(self):
        input_test_string = '1\n2,3\n4'
        expected_number_response = 10
        response_number = self.string_calculator.add(input_test_string)
        self.assertEqual(response_number, expected_number_response)
    
    def test_string_calculator_negative_values_delimited(self):
        input_test_string = '-1,2,-3'
        expected_value_raised = 'negatives not allowed: -1,-3'
        with self.assertRaises(Exception) as context:
            self.string_calculator.add(input_test_string)
        self.assertTrue(expected_value_raised in str(context.exception))

# Verbosity lvl2 lets us get the help string of each test and the result
# on the first log's lines for better understanding when some tests fail
# even when all tests pass
unittest.main(verbosity=2)