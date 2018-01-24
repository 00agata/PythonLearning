'''
Created on 23 sty 2018

@author: agata.wiewiora

This program reads two numbers: length of the base and the height of a right-angled triangle
 and prints the area of this triangle
 
'''

print ('Podaj wielkosc podstawy trojkata')
a = int(input())
print ('Podaj wysokosc trojkata')
h = int(input())
pole = (a * h) / 2
print ('Pole trojkata o podstawie %i i wysokosci %i jest rowne %i' % (a, h, pole))
print (pole)
