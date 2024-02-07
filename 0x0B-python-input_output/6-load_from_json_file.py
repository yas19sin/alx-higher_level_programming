#!/usr/bin/python3
"""
Load from JSON file module
"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
