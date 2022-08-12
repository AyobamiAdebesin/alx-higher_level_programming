#!/usr/bin/env python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1,2,3]
save_to_json_file(my_list, filename)

