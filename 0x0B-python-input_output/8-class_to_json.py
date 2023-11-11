#!/usr/bin/python3
def class_to_json(obj):
    """Returns the dictionary description with
        simple data structure for JSON serialization of an object
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        return obj
