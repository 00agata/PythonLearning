'''
Given a string consisting of words separated by spaces.
Determine how many words it has.
To solve the problem, use the method count()
'''


sample_string = 'Ala ma kota'

# works only, if there is one space character between two words in sample string


def count_words_in_a_string(sample_string):
    words_amount = sample_string.count(" ") + 1
    return words_amount


print(count_words_in_a_string(sample_string))
