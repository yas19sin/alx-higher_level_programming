#!/usr/bin/python3
from sys import argv

args_len = len(argv) - 1
print("{:d} argument{:s}{:s}".format(
    args_len,
    "s" if args_len != 1 else "",
    ":" if args_len > 0 else "."
))

for i in range(1, args_len + 1):
    print("{:d}: {:s}".format(i, argv[i]))
