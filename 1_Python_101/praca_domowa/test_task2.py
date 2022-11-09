import unittest
from collections import namedtuple

from task2 import (
    basic_int_operations,
    string_length,
    first_and_last_chars,
    string_capitalization,
    add_exclamation_mark,
    cut_string,
)

class TestBasicIntOperations(unittest.TestCase):
    Input = namedtuple("Input", ["a", "b"])
    Output = namedtuple(
        "Output", ["sum", "difference", "product", "quotient"]
    )

    TEST_CASES = [
        (
            Input(1, 1),
            Output(2, 0, 1, 1),
        ),
        (
            Input(0, 12),
            Output(12, -12, 0, 0),
        ),
        (
            Input(-10, 4),
            Output(-6, -14, -40, -2)
        )
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(a=input.a, b=input.b):
                self._single_case_test(input, expected_result)

    def _single_case_test(self, input, expected_result):
        result = basic_int_operations(*input)
        for value in result:
            self.assertIsInstance(value, int)
        
        self.assertEquals(result, expected_result)


class TestStringLength(unittest.TestCase):
    TEST_CASES = [
        ("This is the way", 15),
        ("", 0),
        ("1", 1),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = string_length(input)
                self.assertEquals(result, expected_result)


class TestFirstAndLastChars(unittest.TestCase):
    TEST_CASES = [
        ("This is the way", ("T", "y")),
        ("Ab", ("A", "b")),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = first_and_last_chars(input)
                self.assertEquals(result, expected_result)


class TestStringCapitalization(unittest.TestCase):
    TEST_CASES = [
        ("I lIkE jaVa AnD pHP", ("I LIKE JAVA AND PHP", "i like java and php")),
        ("a", ("A", "a")),
        (
            "But I'm Out Of My Head When You're Not Around OOOUUUOOO",
            (
                "BUT I'M OUT OF MY HEAD WHEN YOU'RE NOT AROUND OOOUUUOOO",
                "but i'm out of my head when you're not around ooouuuooo"
            )
        )
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = string_capitalization(input)
                self.assertEquals(result, expected_result)


class TestAddExclamationMark(unittest.TestCase):
    TEST_CASES = [
        ("Daftcode", "Daftcode!"),
        ("Python!", "Python!"),
        ("Don't abuse mocks!!!", "Don't abuse mocks!!!"),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = add_exclamation_mark(input)
                self.assertEquals(result, expected_result)


class TestCutString(unittest.TestCase):
    TEST_CASES = [
        ("Daftcode", "Daftcode"),
        ("python", ""),
        ("BLOOD FOR THE BLOOD GOD", "BLOOD FOR THE BLOOD GOD"),
        ("SKULLS FOR THE pythonSKULL THRONE", "SKULLS FOR THE SKULL THRONE"),
        ("pythonpython", "python"),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = cut_string(input)
                self.assertEquals(result, expected_result)
