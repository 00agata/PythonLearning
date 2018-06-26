'''
Phone number validator - write phone number validator
that accepts phone numbers in not separated,
space-separated or hypen-separated 9-digit
format with optional country prefix
'''

import re

sample_phone_number = '0048 123 456 789'


def phone_number_validator(sample_phone_number):
    phoneRegex = re.compile(r'''(
        (\+\d{0,2}|00[0-9]{0,2})?          # are code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)?                    # separator
        \d{3}                         # second 3 digits
        (\s|-|\.)?                    # separator
        \d{3}                         # last 3 digits
        )''', re.VERBOSE)
    mo = phoneRegex.search(sample_phone_number)
    if mo is not None:
        print(mo.group())


phone_number_validator(sample_phone_number)
