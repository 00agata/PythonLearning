# in order to test PhoneNumberValidator


import pytest
import re

sample_phone_number = '0048 123 456 789'


def phone_number_validator(sample_phone_number):
    phoneRegex = re.compile(r'''(
        (\+\d{0,2}|00[0-9]{0,2})?     # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)?                    # separator
        \d{3}                         # second 3 digits
        (\s|-|\.)?                    # separator
        \d{3}                         # last 3 digits
        )''', re.VERBOSE)
    mo = phoneRegex.match(sample_phone_number)
    if mo is not None:
        print("Phone number is valid")
        print(mo.group())
        return True
    else:
        print("Phone number is not valid")
        return False


def test_phone_number_validator():
    print('Test zero length')
    assert phone_number_validator(0, 0, 0, 0) == 0
    print('Test negative coordinates')
    assert phone_number_validator(-1, -1, -4, -6) == 2
    print('Test vertical distance')
    assert phone_number_validator(0, 0, 4, 6) == 2
    print('Test horizontal distance')
    assert phone_number_validator(4, 6, 0, 0) == 2
    print('Test normal conditions - difference on both coordinates')
    assert phone_number_validator(4, 6, 1, 0) == math.sqrt((6-4)**2 + (0-1)**2)
    print('Test that the order of points does not matter')
    assert phone_number_validator(6, 4, 1, 0) == distance_between_points(4, 6, 1, 0)
