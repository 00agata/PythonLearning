'''
Created on 28 sty 2018

@author: agata.wiewiora

This program that reads an integer number and prints its 
previous and next numbers.

'''


# Read an integer:
integer_ = input("Please, provide sample integer: ")
if '.' in str(integer_):
    print ("This value is invalid. Program finished.")
else:  
    integer_ = int(integer_)
    # Print previous int:
    prev_integer_ = integer_ - 1
    print ("Previous integer: {}").format(prev_integer_)
    # Print next int:
    next_integer_ = integer_ + 1
    print ("Next integer: {}").format(next_integer_)
