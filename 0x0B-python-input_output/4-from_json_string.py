#!/usr/bin/python3
import json

def from_json_string(my_str):
    """A function that returns an object(Python data structure)
    reprsented by a JSON string
    """
    return json.loads(my_str)