#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            print(chr(ord(char) - ord('a') + ord('A')), end="")
        else:
            print(char, end="")
    print()
