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


def get_valid_file_path():
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
    data_read = file_to_modify.read(1024)
    return data_read


def write_data_to_the_file(new_file, data_write, offset):
    new_file.seek(offset)
    amount_of_characters = new_file.write(data_write)
    return amount_of_characters


def parse_data(data_to_search, word):
    while True:
        if word in data_to_search:
            idx = data_to_search.index(word)
            new_word = prompt_substitute(word)
            data_to_search = data_to_search[0:idx] + new_word + data_to_search[(idx+len(new_word)):]
        else:
            return data_to_search
            break

# start script


words = ['ADJECTIVE', 'ADVERB', 'NOUN', 'VERB']


file_path = get_valid_file_path()
path, file = os.path.split(file_path)
new_file = path.append('new' + file)
file_to_modify = open_file()
file_size = os.path.getsize(file_to_modify)
if file_size <= 1024:
    our_data = read_data_from_the_file(file_to_modify, 0)
    for word in words:
        our_data = parse_data(our_data, word)
    write_data_to_the_file(new_file, our_data, 0)
else:
    part = file_size/1024
    for i in range(0, part):
        our_data = read_data_from_the_file(file_to_modify, part*1024)
        for word in words:
            our_data = parse_data(our_data, word)
        write_data_to_the_file(new_file, our_data, part*1024)
        

