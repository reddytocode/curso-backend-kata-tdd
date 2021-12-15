from unittest import TestCase
import unittest
from greeter import Greeter
from freezegun import freeze_time


class GreeterTest(TestCase):
    @freeze_time("2012-01-01 13:45:01")
    def test_greet(self):
        test_name = "Daniel"
        expected_greet = f"Hello {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 13:45:01")
    def test_greet_trims_input(self):
        test_name = "    Raquel "
        expected_greet = "Hello Raquel"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 13:45:01")
    def test_greet_capitalize_input(self):
        test_name = "sebas"
        expected_greet = "Hello Sebas"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 07:45:01")
    def test_greet_good_morning(self):
        test_name = "Daniel"
        expected_greet = f"Good morning {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 19:45:01")
    def test_greet_good_evening(self):
        test_name = "Daniel"
        expected_greet = f"Good evening {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 00:45:01")
    def test_greet_good_night(self):
        test_name = "Daniel"
        expected_greet = f"Good night {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)


unittest.main()
