#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Printing first and last name
    Args:
        first_name = firstName
        last_name = lastName
    Raises:
        typeError if first or last name is not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
