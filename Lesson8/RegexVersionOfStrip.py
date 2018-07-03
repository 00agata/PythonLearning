'''
Write a function that takes a string and does the same thing
as the strip() string method.
If no other arguments are passed other than the string to strip,
then whitespace characters will be removed
from the beginning and end of the string.
Otherwise, the characters specified in the second argument to the
function will be removed from the string.
'''

import re


def strip(sample_string, *args):
    if len(args) is not 0:
        for inputs in args:
            new_regex = re.compile(r'{}'.format(inputs))
            sample_string = (new_regex.sub(r'', '{}'.format(sample_string)))
        return sample_string
    else:
        new_regex = re.compile(r'\s')
        return new_regex.sub(r'', '{}'.format(sample_string))


print(strip('Ala ma      kota'))
