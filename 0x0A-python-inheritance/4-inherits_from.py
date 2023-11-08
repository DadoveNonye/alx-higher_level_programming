#!/usr/bin/python3

"""Defines an istance of a class"""

def inherits_from(obj, a_class):
    """object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        Args: 
            obj: object to check
            a_class: class to check

        returns:
         True if isinstance else False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
