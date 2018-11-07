import unittest

a = int(input('Provide integer: '))
n = int(input('Provide integer: '))


def power(a, n):
    b = 1
    if a == 0:
        return 0
    if (n == 0):
        b = 1
    for i in range (1, abs(n)+1):
        b = b*a
    if (n < 0):
        b = 1/b
    return b

print(power(a,n))


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(power(0,0), 0)
        self.assertEqual(power(2,0), 1)
        self.assertEqual(power(2,3), 8)
        self.assertEqual(power(2,-3), (1/8))
