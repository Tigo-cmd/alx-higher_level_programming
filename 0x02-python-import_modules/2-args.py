#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(n))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
