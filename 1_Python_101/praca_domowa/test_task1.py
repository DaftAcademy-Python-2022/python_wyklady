import unittest

from task1 import (
    return_int,
    return_string,
    return_float,
    convert_to_int,
    return_false,
    return_complex,
)


class TestReturnInt(unittest.TestCase):
    def test_default_case(self):
        result = return_int()
        self.assertIsInstance(result, int)

class TestReturnString(unittest.TestCase):
    def test_default_case(self):
        result = return_string()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 4)

class TestReturnFloat(unittest.TestCase):
    def test_default_case(self):
        result = return_float()
        self.assertIsInstance(result, float)
        self.assertTrue(-1 < result < 1)

class TestReturnFalse(unittest.TestCase):
    def test_dafult_case(self):
        result = return_false()
        self.assertIs(result, False)


class TestConvertToInt(unittest.TestCase):
    TEST_CASES = [
        ("11", 11),
        ("5324", 5324),
        ("-11", -11),
        ("0", 0),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = convert_to_int(input)
                self.assertIsInstance(result, int)
                self.assertEquals(result, expected_result)

class TestReturnComplex(unittest.TestCase):
    TEST_CASES = [0, 34, 11, 5235 -11111]

    def test_multiple_cases(self):
        for input in self.TEST_CASES:
            with self.subTest(input=input):
                result = return_complex(input)
                self.assertIsInstance(result, complex)
                self.assertEquals(input, int(result.real))
