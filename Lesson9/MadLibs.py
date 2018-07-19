'''
Create a Mad Libs program that reads in text files and lets the
user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.

The program would find these occurrences and prompt
the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed.
A nearby pickup truck was unaffected by these events.

The results should be printed to the screen and saved
to a new text file.
'''


import os
from os import path


def prompt_substitute(word_to_substitute):
    if word_to_substitute is 'ADJECTIVE':
        new_word = str(input('Enter adjective: '))
        return new_word
    elif word_to_substitute is 'NOUN':
        new_word =  str(input('Enter noun: '))
        return new_word
    elif word_to_substitute is 'ADVERB':
        new_word = str(input('Enter adverb: '))
        return new_word
    elif word_to_substitute is 'VERB':
        new_word =  str(input('Enter verb: '))
        return new_word
    else:
        return None


def get_valid_file_name():
    while True:
        file_path = str(input('Please, provide file path: '))
        if os.path.isfile(file_path) is True:
            return file_path
            break


def open_file(file_path):
    file_to_modify = open(file_path)
    return file_to_modify


def read_data_from_the_file(file_to_modify, offset):
    file_to_modify.seek(offset)
    data_line = file_to_modify.read(1024)
    return data_line


def write_data_to_the_file(new_file, data, offset):
    new_file.seek(offset)
    amount_of_characters = new_file.write(data)
    return amount_of_characters


def parse_data(data, word):
    data_list = data.split()
    while True:
        if word in data_list:
            idx = data_list.index(word)
            new_word = prompt_substitute(word)
            data_list[idx] = new_word
        else:
            return data_list
            break

