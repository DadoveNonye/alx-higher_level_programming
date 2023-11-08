#!/usr/bin/python3

"""Define a class function"""
def is_same_class(obj, a_class):
    """checks object is exactly an instance of the specified class
        Args:
            obj: object to check
            a_class: class to check
        return:
            True if object is exactly an instance of the specified class
            else
            False
    """
    if type(obj) == a_class:
        return True
    return False
