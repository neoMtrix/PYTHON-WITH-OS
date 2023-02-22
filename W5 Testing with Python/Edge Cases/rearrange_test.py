#!/usr/bin/env/ python3
from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    # EDGES CASES are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with.
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()

# TO RUN IN LINUX:
# chmod +x rearrange_test.py
# ./rearrange_test.py

# TO RUN IN WINDOWS:
# py rearrange_test.py

# OUTPUT:
# ======================================================================
# ERROR: test_empty (__main__.TestRearrange.test_empty)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\user\Desktop\GOOGLE_PYTHON\Using Python to Interact with the Operating\Testing with Python\Unit Test\rearrange_test.py", line 15, in test_empty
#     self.assertEqual(rearrange_name(testcase), expected)
#                      ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\Desktop\GOOGLE_PYTHON\Using Python to Interact with the Operating\Testing with Python\Unit Test\rearrange.py", line 8, in rearrange_name in rearrange_name
#     return "{} {}".format(result[2], result[1])
#                           ~~~~~~^^^
# TypeError: 'NoneType' object is not subscriptable

# ----------------------------------------------------------------------
# Ran 2 tests in 0.002s

# FAILED (errors=1)
#######################################################################
# OUTPUT AFTER HANDLED:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK
