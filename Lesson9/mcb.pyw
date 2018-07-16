#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.


import sys, pyperclip,shelve

mcbShelf = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if [sys.argv[2]] in mcbShelf.keys():
        del mcbShelf[[sys.argv[2]]]
    else:
        print('There is no such key in shelf file')
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # List keywords and load content.
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.close()
        mcbShelf = shelve.open('mcb', flag='n')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
