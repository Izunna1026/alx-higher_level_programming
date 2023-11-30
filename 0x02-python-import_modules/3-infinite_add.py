#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    k = 0
    for l in range(len(sys.argv) - 1):
        k += int(sys.argv[l + 1])
    print("{}".format(k))
