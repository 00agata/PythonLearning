
spam = ['apples', 'bananas', 'tofu', 'cats']


def make_a_sentence(sample_list):
    sample_string = ''
    if sample_list is not None:
        sample_string = ", ".join(sample_list[:-1])
        sample_string = sample_string + " and " + str(sample_list[-1])

    return sample_string


print(make_a_sentence(spam))
