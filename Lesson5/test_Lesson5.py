'''
Test class for ABSwP functions
'''


import unittest
import ABSwP_chapter4_1
import GreaterThanNeighbours
import SwapMinAndMax


class TestCommaCode(unittest.TestCase):

    def test_if_expected_exception_int(self):
        print('Test, if exception will be raised,\
                if input value is an int')

        with self.assertRaises(TypeError):
            ABSwP_chapter4_1.comma_code(5)

    def test_if_expected_exception_None(self):
        print('Test, if exception will be raised,\
                if input value is None')

        with self.assertRaises(TypeError):
            ABSwP_chapter4_1.comma_code(None)

    def test_if_expected_exception_one_string(self):
        print('Test, if exception will be raised,\
                if input value is one string')

        with self.assertRaises(TypeError):
            ABSwP_chapter4_1.comma_code('ala')

    if __name__ == '__main__':
        +    unittest.main()


class TestGreaterThanNeighbours(unittest.TestCase):

    if __name__ == '__main__':
        +    unittest.main()


class TestSwapMinAndMax(unittest.TestCase):

    if __name__ == '__main__':
        +    unittest.main()