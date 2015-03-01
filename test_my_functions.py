import unittest

from my_functions import addition


class MyFunctionsTest(unittest.TestCase):

    def test_addition_function_should_return_sum(self):
        self.assertEqual(addition(2, 3), 5)
