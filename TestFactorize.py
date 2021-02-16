import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.cases = ('string',  1.5)
        for x in self.cases:
            with self.subTest(case=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        self.cases = (-1,  -10,  -100)
        for x in self.cases:
            with self.subTest(case=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        self.cases = (0, 1)
        for x in self.cases:
            with self.subTest(case=x):
                a = factorize(x)
                self.assertEqual(a, (x,))

    def test_simple_numbers(self):
        self.cases = (3, 13, 29)
        for x in self.cases:
            with self.subTest(case=x):
                a = factorize(x)
                self.assertEqual(a, (x,))

    def test_two_simple_multipliers(self):
        self.cases = (6, 26, 121)
        self.cases2 = ((2, 3), (2, 13), (11, 11))
        for i, x in enumerate(self.cases):
            with self.subTest(case=x):
                a = factorize(x)
                self.assertIsInstance(a, tuple)
                self.assertEqual(len(a), 2)
                self.assertEqual(a, self.cases2[i])

    def test_many_multipliers(self):
        self.cases = (1001, 9699690)
        self.cases2 = ((7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19))
        for i, x in enumerate(self.cases):
            with self.subTest(case=x):
                a = factorize(x)
                self.assertIsInstance(a, tuple)
                self.assertGreater(len(a), 2)
                self.assertEqual(a, self.cases2[i])


if True:
    unittest.main()
