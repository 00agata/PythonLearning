'''
Write a function that uses regular expressions to make sure the
password string it is passed is strong. A strong password is
defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least
one digit. You may need to test the string against
multiple regex patterns to validate its strength.
'''

import re


sample_pasword = 'alamaZkota123'


def validate_password(sample_password):

    # check length:
    if len(sample_password) < 8:
        print('Password is too short')
        return False

    # check, if contains lowercase letters
    new_regex = re.compile(r'[+a-z]')
    mo = new_regex.search(sample_pasword)
    if mo is None:
        print('Password does not contain small letters')
        return False

    # check, if contains uppercase letters
    new_regex = re.compile(r'[+A-Z]')
    mo = new_regex.search(sample_pasword)
    if mo is None:
        print('Password does not contain uppercase letters')
        return False

    # check, if contains digits
    new_regex = re.compile(r'[+\d]')
    mo = new_regex.search(sample_pasword)
    if mo is not None:
        print('Password is strong enough')
        return True
    else:
        print('Password does not contain any digits')
        return False


print(validate_password(sample_pasword))
