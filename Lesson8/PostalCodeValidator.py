# Postal code validator
# - write postal code validator that checks if supplied

import re

sample_postal_code = '10-578'


def postal_code_validate(sample_postal_code):
    postalRegex = re.compile(r'^\d{2}-\d{3}$')
    mo = postalRegex.search(sample_postal_code)
    if mo is not None:
        print('Postal code is valid')
        print(mo.group())
        return True
    else:
        print('Postal code is not valid')
        return False


postal_code_validate(sample_postal_code)
