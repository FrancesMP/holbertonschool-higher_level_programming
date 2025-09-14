#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = count = 0
    while True:
        try:
            if count == x:
                break
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                count += 1
            i += 1
        except IndexError:
            break
    print()
    return count
