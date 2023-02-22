#!/usr/bin/env/ python3

import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    # to handle edge case
    if result is None:
        return ""
    return "{} {}".format(result[2], result[1])
