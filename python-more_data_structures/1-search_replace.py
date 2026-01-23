#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return[replace if item == search else item for item in my_list ]

""" def search_replace(my_list, search, replace):
    new_list = []  # make a new list to store results
    
    for item in my_list:          # go through each element
        if item == search:        # check if it matches the search value
            new_list.append(replace)  # add the replacement
        else:
            new_list.append(item)     # otherwise keep the original
    
    return new_list  # return the new list """
