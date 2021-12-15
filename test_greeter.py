import unittest
from greeter import Greeter
from freezegun import freeze_time


class GreeterTest(unittest.TestCase):
    @freeze_time("2012-01-01 07:45:01")
    def test_greet(self):
        test_name = "Daniel"
        expected_greet = f"Good morning {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 07:45:01")
    def test_greet_trims_input(self):
        test_name = "    Raquel "
        expected_greet = "Good morning Raquel"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 07:45:01")
    def test_greet_capitalize_input(self):
        test_name = "sebas"
        expected_greet = "Good morning Sebas"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    @freeze_time("2012-01-01 07:45:01")
    def test_greet_good_morning(self):
        test_name = "Daniel"
        expected_greet = f"Good morning {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)


unittest.main()
