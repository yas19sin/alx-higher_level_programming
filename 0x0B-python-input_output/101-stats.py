#!/usr/bin/python3
""" Reads from standard input and computes metrics """


def print_stats(size, status_codes):
    """ Print accumulated metrics """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 0

            count += 1

            tokens = line.split()
            if len(tokens) >= 2:
                try:
                    size += int(tokens[-1])
                except ValueError:
                    pass

                status_code = tokens[-2]
                if status_code in valid_codes:
                    status_codes[status_code] = (
                            status_codes.get(status_code, 0) + 1)

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
