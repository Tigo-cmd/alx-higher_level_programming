#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception:", file=sys.stderr)
        print("{} is not an integer".format(value), file=sys.stderr)
