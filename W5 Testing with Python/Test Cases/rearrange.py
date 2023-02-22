#!/usr/bin/env/ python3

import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    # TO HANDLE TESTCASE[4]
    if result is None:
        # return ""
        return name
    return "{} {}".format(result[2], result[1])
