import unittest


# function to be tested - from Lesson3
def collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result


class TestCollatz(unittest.TestCase):

    def test_if_expected_value(self):
        print('Test, if collatz(number) function will '
              'return expected value')
        print(self.assertEqual(collatz(8), 4, 'Invalid output value'))
        print(self.assertEqual(collatz(5), 16, 'Invalid output value'))

    def test_input_value(self):
        print('Test that collatz(number) fails when the argument '
              'is not a number')
        with self.assertRaises(TypeError):
            collatz('aoeu')


if __name__ == '__main__':
    unittest.main()
