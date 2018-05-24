'''

Return the word with capital letters

'''


word = 'alicja'


def capitalize(sample_word):
    characters_list = list(sample_word)
    character_ASCII_code = ord(characters_list[0])
    characters_list[0] = chr(character_ASCII_code -32)
    print(''.join(characters_list))


sample_text = 'ala ma kota'

words_list = sample_text.split(' ')

for word in words_list:
    capitalize(word)
