#!/usr/bin/python3
"""Module"""

import sys
import os
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_data = []

arg_to_add = sys.argv[1:]
update_data = existing_data + arg_to_add

save_to_json_file(update_data, "add_item.json")
