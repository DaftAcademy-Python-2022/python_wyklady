import unittest

from task5 import (
    concat_chars,
    concat_chars_not_in_set,
    for_else,
    list_comprehension_odd,
    list_comprehension_sets,
    sum_until,
    double_until_value,
)


class TestConcatChars(unittest.TestCase):
    TEST_CASES = [
        (["a", "b", "c", "d", "e", "f"], "abcdef"),
        ([], ""),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = concat_chars(input)
                self.assertEquals(result, expected_result)

class TestConcatCharsNotInSet(unittest.TestCase):
    TEST_CASES = [
        (
            (["a", "b", "c", "d", "e", "f"], {"a", "b"}), "cdef"),
            (([], set()), ""),
            ((["p", "b", "y", "t", "a", "h", "o", "z", "n"], {"b", "a", "z"}), "python")
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = concat_chars_not_in_set(*input)
                self.assertEquals(result, expected_result)


class TestSumUntil(unittest.TestCase):
    TEST_CASES = [
        (([], 1), 0),
        (([13, 1, 4, 5], 13), 0),
        (([1, 1, 1, 13, 4, 5], 4), 16),
        (([1, 2, 3, 4], 111), 10),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = sum_until(*input)
                self.assertEquals(result, expected_result)


class TestDoubleUntilValue(unittest.TestCase):
    TEST_CASES = [
        (10, 160),
        (1, 128),
        (7, 112),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = double_until_value(input)
                self.assertEquals(result, expected_result)

class TestForElse(unittest.TestCase):
    TEST_CASES = [
        ([], False),
        ([13, 90, 42, 12], False),
        ([1, 1, 1, 1, 10, 1, 1], True),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = for_else(input)
                self.assertIs(result, expected_result)


class TestListComprehensionOdd(unittest.TestCase):
    def test_dafult_case(self):
        result = list_comprehension_odd()
        self.assertEqual(result, [1, 3, 5, 7, 9])


class TestListComprehensionSets(unittest.TestCase):
    TEST_CASES = [
        ((set(), set()), list(range(21))),
        (
            ({1, 2, 3, 4, 5, 6}, {14, 15, 16, 17, 18, 19}), 
            [0, 7, 8, 9, 10, 11, 12, 13, 20]
        )
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = list_comprehension_sets(*input)
                self.assertEquals(result, expected_result)
