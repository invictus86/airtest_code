import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    with open("html.html", "w") as f:
        runner = HTMLTestRunner(stream=f, title="math", description="11", verbosity=2)
    runner.run(suit)
