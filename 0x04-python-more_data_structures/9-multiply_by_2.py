#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_val = {}
    for key, value in a_dictionary.items():
        multi_val[key] = value * 2
    return multi_val
