#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 1
    argcount = len(sys.argv) - 1
    if len(sys.argv) == 2:
        print("1 argument:\n{}: {}".format(count, sys.argv[1]))
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argcount))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(count, sys.argv[i]))
            count = count + 1
