#!/usr/bin/python3

"""Defines a class"""
def is_kind_of_class(obj, a_class):

    """object is an instance of, or if the
        object is an instance of a class
    Args:
        obj: obj to check
        a_class: class to check
    returns:
        True if isinstance else false
    """

    if isinstance(obj, a_class):
        return True
    return False
