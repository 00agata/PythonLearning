# write email validator that checks if supplied
# string is valid e-mail address

import re

sample_email = 'agata.wiewiora1@gmail.com'


def email_validator(sample_email):
    emailRegex = re.compile(r'''(
         [a-zA-Z0-9._%+-]+      # username
         @                      # @ symbol
         [a-zA-Z0-9.-]+         # domain name
           (\.[a-zA-Z]{2,4})    # dot-something
           )''', re.VERBOSE)
    mo = emailRegex.search(sample_email)
    if mo is not None:
        print(mo.group())
        print('Email address is valid')
    else:
        print('Email address is not valid')


email_validator(sample_email)