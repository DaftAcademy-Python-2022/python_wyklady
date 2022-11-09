import unittest

from task7_solution import subsets_everywhere


class TestSubsetsEverywhere(unittest.TestCase):
    TEST_CASES = [
        (
            {1, 2, 3},
            {
                frozenset(),
                frozenset({1}),
                frozenset({2}),
                frozenset({3}),
                frozenset({1,2}),
                frozenset({2,3}),
                frozenset({1,3}),
                frozenset({1,2,3}),
            }
        ),
        (set(), set({frozenset()})),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = subsets_everywhere(input)
                self.assertEqual(result, expected_result)
