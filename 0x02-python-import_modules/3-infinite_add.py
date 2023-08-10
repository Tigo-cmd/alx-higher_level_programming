#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    added = 0
    if len(sys.argv) == 1:
        print("{}".format(added))
    else:
        for i in range(1, len(sys.argv)):
            added += int(sys.argv[i])
        print("{}".format(added))
