#!/usr/bin/python3
"""
    Load, add, save module
"""
if __name__ == "__main__":

    import sys
    import json

    load_json = __import__('8-load_from_json_file').load_from_json_file
    save_json = __import__('7-save_to_json_file').save_to_json_file

    filename = "add_item.json"

    try:
        my_list = load_json(filename)
    except:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_json(my_list, filename)
