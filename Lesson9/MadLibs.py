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


def get_valid_file_name():
    while True:
        file_path = str(input('Please, provide file path: '))
        if os.path.isfile(file_path) is True:
            return file_path
            break


def open_file(file_path):
    file_to_modify = open(file_path)
    return file_to_modify


def parse_file(file_to_modify):
    file_to_modify.