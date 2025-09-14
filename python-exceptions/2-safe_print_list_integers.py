#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = printed = 0
    while count < x:
        try:
            if isinstance(my_list[count], int):
                print("{:d}".format(my_list[count]), end='')
                printed += 1
        except IndexError:
            break
        count += 1
    print()
    return printed
