'''
Created on 28 sty 2018

@author: agata.wiewiora

This program that reads an integer number and prints its 
previous and next numbers.

'''


try:
    # Read an integer:
    integer = raw_input("Please, provide sample integer: ")
    integer = int(integer)
    # Print previous int:
    prev_integer = integer - 1
    print ("Previous integer: {}".format(prev_integer))
    # Print next int:
    next_integer = integer + 1
    print ("Next integer: {}".format(next_integer))
    
    
except ValueError:
    print ("Provided value is invalid. Program finished.")