'''
Write a program that finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on, in a single folder
and locates any gaps in the numbering (such as if there
is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
'''

import shutil

import os


def check_if_dir_path_is_valid (dir1_path):
    isValid1 = os.path.isdir(dir1_path)
    return isValid1


def find_similar_files(dir_path, common_part):
    list_of_similar_files = {}

    for folderName, subfolders, filenames in os.walk(dir_path):
        print('The current folder is {}, files to order: {}'.format(folderName, common_part))

        for filename in filenames:
            print(filename)
            if common_part in filename:
                list_of_similar_files[filename] = ''.join(list(set(filename.split()) - set(common_part.split())))
                print('{} : {}'.format(filename, list_of_similar_files[filename]))

    return list_of_similar_files


def fill_the_gaps(list_of_similar_files):

    for i in range(1, len(list_of_similar_files.values())+1):
        prefix_previous = int((list_of_similar_files.values())[i-1])
        prefix_current = int((list_of_similar_files.values())[i])

        if (prefix_current - prefix_previous) > 0:
            if (prefix_current - prefix_previous) > 1:
                prefix_current = prefix_previous + 1
                for filename, prefix in list_of_similar_files.items():
                    if prefix == prefix_current:
                        list_of_similar_files[filename] == prefix_current
        else:
            print('Wrong numbering of the files')

    return list_of_similar_files


isValid = True;


while True:
    dir_path = str(input('Please, provide valid directory path: '))
    if check_if_dir_path_is_valid(dir_path) is True:
        break
common_part = str(input('Please, provide valid common_part: '))

list_of_files = find_similar_files(dir_path, common_part)

if (list_of_files is not None):
    fill_the_gaps(list_of_files)
else:
    print('No files with provided prefix')
