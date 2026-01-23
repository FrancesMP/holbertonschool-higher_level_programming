#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # : Retrieve and sort the keys
    sorted_keys = sorted(a_dictionary.keys())
    
    # : Loop through sorted keys
    for key in sorted_keys:
        # : Print each key-value pair
        print(f"{key}: {a_dictionary[key]}")
