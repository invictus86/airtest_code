import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1, 2))

    def test_minus(self):
        self.assertEqual(1, minus(3, 2))


if __name__ == '__main__':
    unittest.main(verbosity=0)
