import unittest

from task4 import (
    simple_conditional,
    zero_comparision,
    list_searching,
    roman_numerals,
)


class TestSimpleConditional(unittest.TestCase):
    TEST_CASES = [
        (10, False),
        (9, False),
        (0, False),
        (-100, False),
        (11, True),
        (1000, True),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = simple_conditional(input)
                self.assertIs(result, expected_result)



class TestZeroComparision(unittest.TestCase):
    TEST_CASES = [
        (10, 1),
        (9, 1),
        (0, 0),
        (-100, -1),
        (11, 1),
        (-1, -1),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = zero_comparision(input)
                self.assertEqual(result, expected_result)


class TestListSearching(unittest.TestCase):
    TEST_CASES = [
        ((1, [1]), True),
        ((100, [99, 100, 101]), True),
        ((11, []), False),
        ((0, [1, 2 ,3]), False),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = list_searching(*input)
                self.assertEqual(result, expected_result)


class TestRomanNumerals(unittest.TestCase):
    TEST_CASES = [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (8, "VIII"),
        (9, "IX"),
        (10, "X"),
        (0, ""),
        (11, ""),
        (-200, ""),
        (1000, ""),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = roman_numerals(input)
                self.assertEqual(result, expected_result)

