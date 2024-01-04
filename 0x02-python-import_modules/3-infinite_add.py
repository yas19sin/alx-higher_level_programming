#!/usr/bin/python3
from sys import argv

args_len = len(argv) - 1
result = sum(int(arg) for arg in argv[1:])
print("{:d}".format(result))
