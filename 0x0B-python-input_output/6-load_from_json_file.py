#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)