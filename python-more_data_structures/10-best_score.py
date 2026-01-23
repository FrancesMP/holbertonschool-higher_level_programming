#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None  # Return None if dictionary is empty or None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key