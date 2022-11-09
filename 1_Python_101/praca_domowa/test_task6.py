import unittest

from task6 import lazy_scribe


class TestLazyScribe(unittest.TestCase):
    TEST_CASES = [
        (["python", "java", "golang"], "pjgyaotvlh2ao2ng"),
        ([], ""),
        ([""], ""),
        (["", "", "", ""], ""),
        (["a", "b", "c", "d"], "abcd"),
        (["yomasoul", "yomaha", "yoma", "tyryryryry", "ryry"], "3ytr3o2y3m2r3a2yshroayurlyry")
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = lazy_scribe(input)
                self.assertEqual(result, expected_result)
