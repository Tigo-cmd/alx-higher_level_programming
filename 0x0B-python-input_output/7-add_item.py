#!/usr/bin/python3
"""this module creates script that adds all arguments to a Python list,
   and then save them to a file
"""


import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

main_file = "add_item.json"
existing = []
if len(sys.argv) > 1:
    existing = load_from_json_file(main_file)
    new_list = sys.argv[1:]
    existing.extend(new_list)
    save_to_json_file(existing, main_file)
else: 
    save_to_json_file(existing, main_file)
