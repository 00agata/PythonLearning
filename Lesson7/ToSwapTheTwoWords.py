'''
Given a string consisting of exactly two words separated by a space.
Print a new string with the first and second word
positions swapped (the second word is printed first).
'''


sample_string_two_words = 'ala ola'


def swap_words_in_two_word_string(sample_string_two_words_with_space):
    list_str = sample_string_two_words_with_space.split(' ')
    list_str_2 = []
    list_str_2.append(list_str[1])
    list_str_2.append(list_str[0])
    str = ' '.join(list_str_2)
    return str


print(swap_words_in_two_word_string(sample_string_two_words))
