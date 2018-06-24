# Postal code validator
# - write postal code validator that checks if supplied

import re

sample_postal_code = '102-578'


def postal_code_validate(sample_postal_code):
    postalRegex = re.compile(r'\d{2}-\d{3}', re.VERBOSE)
    mo = postalRegex.search(sample_postal_code)
    if mo is not None:
        print(mo.group())
        print('Postal code is valid')
    else:
        print('Postal code is not valid')


postal_code_validate(sample_postal_code)
