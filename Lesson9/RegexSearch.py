'''
Write a program that opens all .txt files in a folder
and searches for any line that matches
a user-supplied regular expression.
The results should be printed to the screen.
'''

import re
import os
from os import listdir
from os.path import isfile, join


def get_valid_directory_path_to_search():
    while True:
        my_path = str(input('Please, provide valid directory path: '))
        if os.path.isdir(my_path) is True:
            return my_path
            break


def get_list_of_the_files_in_given_directory(my_path):
    only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    return only_files


def get_valid_regex():
    while True:
        reg_ex = str(input('Please, provide valid regex: '))
        try:
            re.compile(reg_ex)
            is_valid = True
        except re.error:
            is_valid = False
        if is_valid is True:
            return reg_ex
            break


def open_file(file_path):
    file = open(file_path)
    return file


def read_data_from_the_file(file, offset):
    file.seek(offset)
    data_read = file.read(1024)
    return data_read

# start script


dir_path = get_valid_directory_path_to_search()
files_list = get_list_of_the_files_in_given_directory(dir_path)

reg_ex = get_valid_regex()

for file in files_list:
    file_size = file_size = os.path.getsize(file)
    if file_size <= 1024:
        our_data = read_data_from_the_file(file, 0)
        mo = reg_ex.search(our_data)
        if mo is None:
            pass
        else:
            for o in mo:
                print(o)
    else:
        part = file_size/1024
        if type(part) == 'int':
            pass
        else:
            part = file_size//1024 + 1
        for i in range(0, part):
            our_data = read_data_from_the_file(file, part*1024)
            mo = reg_ex.search(our_data)
            if mo is None:
                pass
            else:
                for o in mo:
                    print(o)
