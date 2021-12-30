import unittest

from utils import factor_pow, gcd, factorize, get_num_from_factor, check_prime, PrimeGenerator, get_digits_from_num, get_num_from_digits

class TestUtils(unittest.TestCase):
    def test_gcd(self):
        inputs = [(461952, 116298), (12, 0), (0, 9), (42, 56)]
        expected_outputs = [18, 12, 9, 14]

        for idx, inp in enumerate(inputs):
            result = gcd(inp[0], inp[1])
            self.assertEqual(result, expected_outputs[idx])

    def test_factorize(self):
        inputs = [16, 17, 147]
        expected_outputs = [[[2, 4]], [[17, 1]], [[3, 1], [7, 2]]]
        for idx, inp in enumerate((inputs)):
            result = factorize(inp)
            with self.subTest(inp = inp, expected = expected_outputs[idx]):
                self.assertListEqual(result, expected_outputs[idx])

    def test_get_num_from_factor(self):
        inputs = [[[2, 4]], [[17, 1]], [[3, 1], [7, 2]]]
        expected_outputs = [16, 17, 147]
        for idx, factors in enumerate((inputs)):
            result = get_num_from_factor(factors)
            with self.subTest(inp = factors, expected = expected_outputs[idx]):
                self.assertEqual(result, expected_outputs[idx])
    
    def test_factor_pow(self):
        n_list = [16, 17, 147]
        powers = [0, 2, 3]

        for n, power in zip(n_list, powers):
            expected = n**power
            factors = factorize(n)
            n_power_factors = factor_pow(factors, power)
            n_power = get_num_from_factor(n_power_factors)
            with self.subTest(inp = n_power_factors, expected = expected):
                self.assertEqual(n_power, expected)

    def test_check_prime(self):
        with self.subTest():
            self.assertEqual(check_prime(3), True)
        with self.subTest():
            self.assertEqual(check_prime(4), False)
        with self.subTest():
            self.assertEqual(check_prime(10000189), True)
        with self.subTest():
            self.assertEqual(check_prime(91), False)
    
    def test_prime_generator(self):
        expected = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
        solution = PrimeGenerator()
        with self.subTest(expected = expected):
            self.assertListEqual(expected, solution.generate_prime_list(len(expected)-1))

    def test_get_digits_from_num(self):
        n, expected = 5, [5]
        with self.subTest(expected = expected):
            self.assertListEqual(expected, get_digits_from_num(n))

        n, expected = 100, [1, 0, 0]
        with self.subTest(expected = expected):
            self.assertListEqual(expected, get_digits_from_num(n))

        n, expected = 1234, [1, 2, 3, 4]
        with self.subTest(expected = expected):
            self.assertListEqual(expected, get_digits_from_num(n))

    def test_get_num_from_digits(self):
        expected, digits = 5, [5]
        with self.subTest(expected = expected):
            self.assertEqual(expected, get_num_from_digits(digits))

        expected, digits = 100, [1, 0, 0]
        with self.subTest(expected = expected):
            self.assertEqual(expected, get_num_from_digits(digits))

        expected, digits = 1234, [1, 2, 3, 4]
        with self.subTest(expected = expected):
            self.assertEqual(expected, get_num_from_digits(digits))
        