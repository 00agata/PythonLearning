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
all_cards = []
remaining_cards = []

if N < 10:
    for number in range(1, N+1):
        all_cards.append(number)
    
    for number in range(1, N):
        n = int(input('provide other card\'s number:' ))
        remaining_cards.append(n)

    lost_card = [card for card in all_cards if card not in remaining_cards]
    
    print('Lost number is {}'.format(lost_card[0]))
else:
    print ('Incorrect input value')
