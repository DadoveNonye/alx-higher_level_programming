#!/usr/bin/python3
"""Defines a dict desp with simple data structure"""
def class_to_json(obj):
    """Returns the dictionary description with
        simple data structure for JSON serialization of an object
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        return obj
