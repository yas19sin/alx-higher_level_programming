#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except (IndexError, TypeError):
            print("out of range" if i >= len(my_list_1) or i >= len(my_list_2) else "wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        finally:
            result.append(division)
    return result
