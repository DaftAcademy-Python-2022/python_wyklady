import unittest
from collections import namedtuple
from task3 import (
    list_declaration,
    list_indexing,
    list_sum,
    dict_declaration,
    dict_pass_values,
    dict_retrieving_values,
    set_add_list,
    set_declaration,
    set_operations,
)


class TestListDeclaration(unittest.TestCase):
    def test_default_case(self):
        result = list_declaration()
        self.assertIsInstance(result, list)

        expected_types = [str, int, float, bool]
        for value, expected_type in zip(result, expected_types):
            self.assertIsInstance(value, expected_type)


class TestListIndexing(unittest.TestCase):
    TEST_CASES = [
        (["a", "b", "c"], ("a", "c")),
        ([2, 41, 532, 21, 52334], (2, 52334)),
        ([1], (1, 1)),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = list_indexing(input)
                self.assertEquals(result, expected_result)


class TestListSum(unittest.TestCase):
    TEST_CASES = [
        ([1, 1, 1], 3),
        ([2, 5, 52334], 52341),
        ([1], 1),
        ([1, -1, 2, -2, 0], 0)
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = list_sum(input)
                self.assertEquals(result, expected_result)


class TestDictDeclaration(unittest.TestCase):
    def test_dafult_case(self):
        result = dict_declaration()
        self.assertEqual(result.get('line_length'), 42)


class TestDictRetrievingValues(unittest.TestCase):
    TEST_CASES = [
        ({"a": 1, "b": 1}, 2),
        ({"a": 1, "b": -11}, -10),
        ({"a": 0, "b": 0}, 0),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = dict_retrieving_values(input)
                self.assertEquals(result, expected_result)


class TestDictPassValues(unittest.TestCase):
    TEST_CASES = [
        (
            ({"variable": 21}, {}),
            {"variable": 21}
        ),
        (
            (
                {"some_trash": False, "variable": 112},
                {"some_other_trash": "agsbfdg"}
            ),
            {"variable": 112, "some_other_trash": "agsbfdg"}
        ),
        (
            (
                {"some_trash": False, "variable": -54},
                {"variable": "agsbfdg"}
            ),
            {"variable": -54}
        )
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = dict_pass_values(*input)
                self.assertEquals(result, expected_result)


class TestSetDeclaration(unittest.TestCase):
    def test_dafult_case(self):
        result = set_declaration()
        for value in result:
            self.assertIsInstance(value, int)


class TestSetOperations(unittest.TestCase):
    Input = namedtuple("Input", ["set_a", "set_b"])
    Output = namedtuple(
        "Output", ["intersection", "union", "difference"]
    )
    TEST_CASES = [
        (
            Input({1, 2, 3}, {3, 4, 5}),
            Output({3}, {1, 2, 3, 4, 5}, {1, 2})
        ),
        (
            Input(set(), {1, 2}),
            Output(set(), {1, 2}, set())
        ),
        (
            Input({1}, {4, 5}),
            Output(set(), {1, 4, 5}, {1})
        ),
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(
                set_a=input.set_a, set_b=input.set_b
            ):
                result = set_operations(*input)
                self.assertEquals(result, expected_result)


class TestSetAddList(unittest.TestCase):
    TEST_CASES = [
        ((set(), []), set()),
        (
            (set(), [1, 2, 3]),
            {1, 2, 3}
        ),
        (
            ({1, 2}, []),
            {1, 2}
        ),
        (
            ({1, 4}, [2, 3, 2, 3, 5]),
            {1, 2, 3, 4, 5}
        )
    ]

    def test_multiple_cases(self):
        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = set_add_list(*input)
                self.assertIsInstance(result, set)
                self.assertEquals(result, expected_result)
