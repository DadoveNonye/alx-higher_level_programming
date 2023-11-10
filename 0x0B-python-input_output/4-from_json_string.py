#!/usr/bin/python3

"""Function that retunrs a python data objrct"""
import json
def from_json_string(my_str):
    """returns an obj"""
    return json.loads(my_str)
