import unittest
from greeter import Greeter


class GreeterTest(unittest.TestCase):
    def test_greet(self):
        test_name = "daniel"
        expected_greet = f"Hello {test_name}"
        self.assertEqual(Greeter().greet(test_name), expected_greet)


unittest.main()
