#!/usr/bin/python3
"""A script that stores arguments to a JSON file"""

from sys import argv
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

namefile = "add_item.json"
args = len(argv)

file_list = []

if exists(namefile):
    file_list = load_from_json_file(namefile)

if (args == 1):
    save_to_json_file(file_list, namefile)
else:
    for index in range(1, args):
        file_list.append(argv[index])
    save_to_json_file(file_list, namefile)
