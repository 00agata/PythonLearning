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
            reg = re.compile(reg_ex)
            is_valid = True
        except re.error:
            is_valid = False
        if is_valid is True:
            return reg
            break


# start script


dir_path = get_valid_directory_path_to_search()

files_list = get_list_of_the_files_in_given_directory(dir_path)

pattern = get_valid_regex()

for file in files_list:
    file_path = os.path.join(dir_path, file)
    file_itself = open(file_path,'r')
    file_content = file_itself.read()
    for match in re.finditer(pattern, file_content):
        print('Found in file: {} match: {}'.format(file, match.group()))
