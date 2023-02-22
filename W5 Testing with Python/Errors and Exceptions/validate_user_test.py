#!/usr/bin/env/ python3

import unittest

from validate_user import validate_user


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)


# Run the tests
unittest.main()

# OUTPUT:
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s

# OK

# In earlier videos, we looked into how we can create unit tests for our functions, for both the basic cases and the edge cases. We called out that we should try to cover lots of different possible cases. To make sure that our function behaves correctly in all of them. With some edge cases, like negative value of minlen in our earlier example, the expectation is that the function will raise an error and we want to be able to test that too. So, how do we do that? Well, we use the assert raises method provided by the unit test module. Let's check this out by adding a couple of test cases to the test suite for our validate user function. This is the existing test suite. As you can see, we've got a few test cases checking that the function is working correctly, when it receives same parameters. We now want to add some other cases for when it receives parameters that don't make sense. Like a negative value for minlen or a username that's a list instead of the string. Let's do that now.

# We can see that the assert raises method works a little bit differently than the assert equal method that we used before. In this case, we need to first pass the error that we expect the function to raise. Then the function name, followed by any parameters that need to be passed to that function. Behind the scenes, this method is calling the function that we want to test using the try except block and checking that it does raise the error that we said it would raise. Okay, let's run this test suite and verify that our code works correctly.
