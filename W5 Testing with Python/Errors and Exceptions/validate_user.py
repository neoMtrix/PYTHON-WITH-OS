#!/usr/bin/env/ python3


def validate_user(username, minlen):
    # TESTCASE[2]
    assert type(username) == str, "username must be string"
    # TESTCASE[1]
    if minlen < 1:
        raise ValueError("minlen  must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True


# Say we had a function that verifies whether a chosen username is valid. One of the checks this function does is verify that the provided name is at least a certain amount of characters with the minimum value received by a parameter. Something like this. In this function, we're first checking that the username variable has at least minlen characters. After checking that, we verify if there are any non-alphanumeric characters in the string which is another criteria for validating a username. If all the checks pass we return true to indicate that the username chosen is valid. This code works as long as the provided values are sensible.
##############
# TESTCASE[1]
# What would happen if the minlen variable is zero or negative number? Our function will allow an empty username as valid which doesn't make much sense. To prevent this from happening, we can add an extra check to our function which will verify the receipt parameters are sane. In this case, returning false would be misleading because it's not necessarily that the username is invalid but the provided minlen value doesn't make sense. So let's add a check to verify that minlen is at least one and raise an error if that's not the case.
################
# TESTCASE[2]
# But in some cases, we might want to do this explicitly by checking that we're receiving a value that makes sense to that function. So let's look at an alternative to the raise keyword that we can use for situations where we want to check that our code behaves the way it should particularly when we want to avoid situations that should never happen.
# This is the assert keyword. This keyword tries to verify that a conditional expression is true, and if it's false it raises an assertion error with the indicated message
# We've added an assertion that verifies that the type of the username variable is STR which we know is a name that the interpreter uses for strings. If the function is called with a username parameter that's not a string, an error will be raised with the message we provided.
