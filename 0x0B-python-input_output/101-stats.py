#!/usr/bin/python3
"""
Log parsing module
"""
import sys


def print_stats(file_size, status_codes):
    """Print statistics"""
    print("File size: {:d}".format(file_size))
    for status, count in sorted(status_codes.items()):
        print("{}: {}".format(status, count))


if __name__ == "__main__":
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split()
            if len(tokens) >= 2:
                try:
                    file_size += int(tokens[-1])
                except ValueError:
                    pass
                status_code = tokens[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(file_size, status_codes)
