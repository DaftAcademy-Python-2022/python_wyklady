import unittest
from task0 import sanity_check_task


class TestSanityCheckTask(unittest.TestCase):
    def test_default_case(self):
        self.assertEqual(sanity_check_task(), 42)
