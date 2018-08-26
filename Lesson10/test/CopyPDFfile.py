'''

'''

import shutil
import os


def check_if_dir_paths_are_valid (dir1_path, dir2_path):
    isValid1 = os.path.isdir(dir1_path)
    isValid2 = os.path.isdir(dir2_path)
    return (isValid1 and isValid2)


def copy_files(dir_path, dir_path_for_copy, filter_extension):
    for folderName, subfolders, filenames in os.walk(dir_path):
        print('The current folder is ' + folderName)

        for filename in filenames:
            whole_path = os.path.join(dir_path, filename)
            if filename.endswith(filter_extension):
                shutil.copy(whole_path, dir_path_for_copy)
                print('{} has been copied to {}'.format(filename, dir_path_for_copy))
                print('')


isValid = True;


while True:
    dir_path = str(input('Please, provide valid directory path: '))
    dir_path_for_copy = str(input('Please, provide valid directory path to copy files to: '))
    if check_if_dir_paths_are_valid(dir_path, dir_path_for_copy) is True:
        break
extension = str(input('Please, provide valid extension e.g. .pdf: '))

copy_files(dir_path, dir_path_for_copy, extension)
