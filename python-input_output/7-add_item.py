#!/usr/bin/python3
import sys
"""
7. Load, add, save
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

liste = sys.argv[1:]
with open('add_item.json', 'w') as f:
    save_to_json_file(liste, f)
    load_from_json_file(f)