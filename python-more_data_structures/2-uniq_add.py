#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_elements = set(my_list)
    b = 0
    for element in unique_elements:
        b = element + b
    return b
