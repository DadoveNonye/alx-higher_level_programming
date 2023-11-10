#!/usr/bin/python3
import json
"""Function that retunrs a python data objrct"""
def from_json_string(my_str):
    """returns an obj"""
    return json.loads(my_str)
