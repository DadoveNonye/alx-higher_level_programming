#!/usr/bin/python3
""" function that adds two integers """
def add_integer(a, b=98):
    """Returns interger addtion of a and b
        A and b must be floats
        Raise:
            typeerror if either a or b is not a int or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError ("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError ("b must be an integer")
    return (int(a) + int(b))
