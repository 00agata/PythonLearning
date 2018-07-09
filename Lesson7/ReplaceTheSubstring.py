'''
Given a string. Replace in this string all the numbers 1 by the word one.
'''

sample_string = '111knknjnk111kjkjh11khkh1'

# substring - string to replace
# sample_string - string to make replacements of substring of this string
# replacement - new string to put instead of substring


def replace_substring(substring, sample_string, replacement):
    sample_list = list(sample_string)
    for idx, item in enumerate(sample_list):
        if item == substring:
            sample_list[idx] = replacement
    return str(sample_list)


print(replace_substring('1', sample_string, 'one'))
