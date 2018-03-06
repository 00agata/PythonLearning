'''
Created on 26 lut 2018

@author: agata.wiewiora

There was a set of cards with numbers from 1 to N. 
One of the card is now lost. 
Determine the number on that lost card given 
the numbers for the remaining cards.

Given a number N, followed by N-1 integers -
representing the numbers on the remaining cards 
(distinct integers in the range from 1 to N). 
Find and print the number on the lost card. 

'''


N = int(input('provide N < 10'))
N_array = []
n_array = []

if N < 10:
    for Ns in range(1, N+1):
        N_array.append(Ns)
    
    for Ns in range(1, N):
        n = int(input('provide other card\'s number:' ))
        n_array.append(n)
        
    lost_number = list(set(N_array) - set(n_array))[0]
    
    print('Lost number is {}'.format(lost_number))
else:
    print ('Incorrect input value')
