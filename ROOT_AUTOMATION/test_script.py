import unittest
import cel_to_fah


class Tests(unittest.TestCase):
    def test_func(self):
        self.assertEqual(cel_to_fah.func(40.00), 104.00)