from unittest import TestCase
import unittest
from string_calculator import StringCalculator


class StringCalculatorTest(TestCase):
    def setUp(self):
        self.string_calculator = StringCalculator()

    def test_string_calculator_zero(self):
        test_string = ''
        expected_number = 0
        self.assertEqual(self.string_calculator.add(test_string), expected_number)


unittest.main(argv=[''],verbosity=2, exit=False)