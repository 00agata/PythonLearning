# in order to test PhoneNumberValidator


import pytest
import re

sample_phone_number = '0048 123 456 789'


def phone_number_validator(sample_phone_number):
    phoneRegex = re.compile(r'''^(
        (\+\d{0,2}|00[0-9]{0,2})?     # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)?                    # separator
        \d{3}                         # second 3 digits
        (\s|-|\.)?                    # separator
        \d{3}                         # last 3 digits
        $)''', re.VERBOSE)
    mo = phoneRegex.match(sample_phone_number)
    if mo is not None:
        print("Phone number is valid")
        print(mo.group())
        return True
    else:
        print("Phone number is not valid")
        return False


print(phone_number_validator(sample_phone_number))


def test_phone_number_validator():
    assert phone_number_validator('2341342342342') is False
    assert phone_number_validator('0048 123 456 789') is True
    assert phone_number_validator('0048 123 456 799989') is False
