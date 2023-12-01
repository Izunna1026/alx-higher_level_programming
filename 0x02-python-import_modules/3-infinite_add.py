#!/usr/bin/python3

if __name__ == "__main__":
    import sys
k = 0
for count in range(len(sys.argv) - 1):
    k += int(sys.argv[count + 1])
print("{}".format(k))
