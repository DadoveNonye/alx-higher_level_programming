#!/usr/bin/python3
"""function that adds new attributes"""
def add_attribute(obj, attr, value):
    """raise error if it can't have new attribute
        Args: obj, attr, value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
