#!/usr/bin/env/ python3
from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    # TESTCASE[1]
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    # TESTCASE[2]
    # EDGES CASES are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with.
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    # TESTCASE[3]
    # In this case, we're testing that someone with more than one given name still gets their name properly rearranged.
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    # TESTCASE[4]
    # In this case this person only has one name, so there's no comma in our string. We expect the result to be the same name we provided to the function.
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()

# TO RUN IN LINUX:
# chmod +x rearrange_test.py
# ./rearrange_test.py

# TO RUN IN WINDOWS:
# py rearrange_test.py

# OUTPUT TESTCASE[3]:
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK

###################################################
# OUTPUT TESTCASE[4]:
# ======================================================================
# FAIL: test_one_name (__main__.TestRearrange.test_one_name)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\user\Desktop\GOOGLE_PYTHON\Using Python to Interact with the Operating\Testing with Python\Test Cases\rearrange_test.py", line 32, in test_one_name
#     self.assertEqual(rearrange_name(testcase), expected)
# AssertionError: '' != 'Voltaire'
# + Voltaire

# ----------------------------------------------------------------------
# Ran 4 tests in 0.002s

# FAILED (failures=1)

# OUTPUT TESTCASE[4] AFTER HANDLED:
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s

# OK
