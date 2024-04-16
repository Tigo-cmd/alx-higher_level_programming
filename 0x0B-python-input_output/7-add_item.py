#!/usr/bin/python3
"""another manipulative function module"""
import sys

if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file
    file = "add_item.json"

    try:
        content = load_from_json(file)
    except FileNotFoundError:
        content = []

    content.extend(sys.argv[1:])
    save_to_json(content, file)
