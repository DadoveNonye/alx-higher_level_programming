#!/usr/bin/python3

"""Defines a class function"""
class Mylist(list):
    """prints the list, in sorted ascending sort"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
