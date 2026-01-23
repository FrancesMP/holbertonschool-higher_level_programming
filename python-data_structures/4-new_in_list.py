#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    elif idx > 0 and idx < len(my_list):
        new_list = my_list[:]  # Crée une copie de la liste
        new_list[idx] = element
    return new_list
