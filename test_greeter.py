import unittest
from greeter import Greeter


class GreeterTest(unittest.TestCase):
    def test_greet(self):
        test_name = "Daniel"
        expected_greet = f"Hello {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    def test_greet_trims_input(self):
        test_name = "    Raquel "
        expected_greet = "Hello Raquel"
        self.assertEqual(Greeter().greet(test_name), expected_greet)

    def test_greet_capitalize_input(self):
        test_name = "sebas"
        expected_greet = "Hello Sebas"
        self.assertEqual(Greeter().greet(test_name), expected_greet)


unittest.main()
