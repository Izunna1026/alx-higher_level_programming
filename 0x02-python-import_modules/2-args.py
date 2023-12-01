#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    k = len(sys.argv) - 1
    if k == 0:
        print("0 arguments.")
    elif k == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(k))
    for count in range(k):
        print("{}: {}".format(count + 1, sys.argv[count + 1]))
