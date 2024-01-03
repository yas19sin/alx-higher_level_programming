#!/usr/bin/python3

for i in range(122, 96, -1):
    if i % 2 == 0:
        letter = i
    else:
        letter = i - 32
    print("{:c}".format(letter), end="")
print()
