
def upper_case_first_letter(word):
    if len(word) < 1:
        return
    list_of_letters = [letter for letter in word]
    ascii_idx = ord(str(list_of_letters[0]))
    print(ascii_idx)
    ascii_idx_upper = ascii_idx - 32
    print(ascii_idx_upper)
    upper_leter = chr(ascii_idx_upper)
    print(upper_leter)
    list_of_letters[0] = upper_leter
    return ''.join(list_of_letters)


sample_text = 'ala ma kota'


def make_words_uppercase(sample_text):
    if len(sample_text) < 2:
        return
    list_of_words = sample_text.split()
    if len(list_of_words) > 0:
        new_list_of_words = [upper_case_first_letter(word) for word in list_of_words]
        return ' '.join(new_list_of_words)


print(make_words_uppercase(sample_text))
