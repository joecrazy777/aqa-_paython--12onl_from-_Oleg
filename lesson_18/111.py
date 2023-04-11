# import unittest
#
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper3(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     @unittest.skip
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     @unittest.expectedFailure
#
#     def test_upper2(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#
# if __name__ == '__main__':
#     unittest.main()


import unittest


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):

    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_10(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_true(self):
        self.assertTrue(factorial(4), True)

    def test_factorial_isnone(self):
        self.assertIsNotNone(factorial(5), True)
