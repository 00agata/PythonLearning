'''
Created on 28 sty 2018

@author: agata.wiewiora

This program that reads an integer number and prints its 
previous and next numbers.

'''


try:
    # Read an integer:
    integer_ = raw_input("Please, provide sample integer: ")
    integer_ = int(integer_)
    # Print previous int:
    prev_integer_ = integer_ - 1
    print ("Previous integer: {}").format(prev_integer_)
    # Print next int:
    next_integer_ = integer_ + 1
    print ("Next integer: {}").format(next_integer_)
    
    
except ValueError:
    print ("Provided value is invalid. Program finished.")
