#!/usr/bin/python3
import sys
if __name__ == "__main__":
    res = 0
    for i in range(1, len(sys.argv)):
        argv = int(sys.argv[i])
        res += argv
    print("{}".format(res))
