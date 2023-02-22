#!/usr/bin/env/ python3
from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()

# TO RUN IN LINUX:
# chmod +x rearrange_test.py
# ./rearrange_test.py

# TO RUN IN WINDOWS:
# py rearrange_test.py

# OUTPUT:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK
