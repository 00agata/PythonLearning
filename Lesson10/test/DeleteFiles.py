'''

'''


import shutil
import os


def check_if_dir_path_is_valid (dir1_path):
    isValid1 = os.path.isdir(dir1_path)
    return isValid1


def print_big_files(dir_path, filter_size):
    print(os.walk(dir_path))
    for folderName, subfolders, filenames in os.walk(dir_path):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            for filename in filenames:
                whole_path = os.path.join(dir_path, filename)

                if os.path.getsize(whole_path) > filter_size:
                    print('{} is bigger than {}'.format(whole_path, filter_size))
                    print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
                    print('FILE INSIDE ' + folderName + ': ' + filename)
                    print('')


isValid = True;


while True:
    dir_path = str(input('Please, provide valid directory path: '))
    if check_if_dir_path_is_valid(dir_path) is True:
        break
file_size_filter = int(input('Please, provide valid file size in MB, e.g. 100: '))

print_big_files(dir_path, file_size_filter)