import unittest


def collatz_function(number):
    if type(number) == int:
        if number % 2 == 0:
            return number
        else:
            return 3 * number + 1
    else:
        raise TypeError


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(collatz_function(2), 2)
        self.assertEqual(collatz_function(3), 10)
        self.assertEqual(collatz_function(0), 0)
        self.assertEqual(collatz_function(-1), -2)

