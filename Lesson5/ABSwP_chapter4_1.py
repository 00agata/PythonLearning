'''
Comma Code

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument
and returns a string with all the items separated by a comma
and a space, with and inserted before the last item.
For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
'''


spam = []


def comma_code(spam):
    spam_string = ", ".join(spam[:-1])
    spam_string = spam_string + ' and ' + spam[-1]
    return spam_string


spam = ['ala', 'ola', 'ula']

joined_string_from_the_list = comma_code(spam)
print(joined_string_from_the_list)
