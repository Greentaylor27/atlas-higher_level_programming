#!/usr/bin/python3
"""
Module that adds all arguments to a Python list then saves them to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
newlist = []

try:
    newlist = load_from_json_file(filename)
except Exception as e:
    pass

for f in range(1, len(sys.argv)):
    newlist.append(sys.argv[f])

save_to_json_file(newlist, filename)
