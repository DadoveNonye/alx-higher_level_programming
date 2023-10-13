#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    for uni in my_list:
        unique.add(uni)
    total = sum(unique)
    return total
