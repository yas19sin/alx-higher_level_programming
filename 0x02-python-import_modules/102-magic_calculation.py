#!/usr/bin/python3
if __name__ == "__main__":
    def magic_calculation(a, b):
        if a < b:
            return add(a, b)
        result = sub(a, b)
        for i in range(4, 6):
            result = add(result, i)
        return result
