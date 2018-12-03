'''
Given a number n, followed by n lines of text,
print the number of distinct words that appear in the text.
For this, we define a word to be a sequence of non-whitespace
characters, seperated by one or more whitespace
or newline characters.
Punctuation marks are part of a word, in this definition.
'''


def count_words(text):
    if text is not None:
        if '\r' in text:
            list_of_lines = text.split('\r')
        if '\n' in text:
            list_of_lines = text.split('\n')
        if '\r\n' in text:
            list_of_lines = text.split('\r\n')
        if len(list_of_lines) > 0:
            list_of_words = [line.split(' ') for line in list_of_lines]
            return sum([len(item) for item in list_of_words])


print(count_words('Ala ma kota\r\nOla ma psa'))
