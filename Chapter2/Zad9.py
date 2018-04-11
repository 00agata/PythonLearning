'''
Created on 13 lut 2018

@author: agata.wiewiora

H hours, M minutes and S seconds are passed since the midnight 
Determine the angle (in degrees) of the hour hand on the clock face right now.

'''


H = int(input('Provide hours:'))
M = int(input('Provide minutes:'))
S = int(input('Provide seconds:'))

M = M + S/60
S = S % 60
H = H + M/60
M = M % 60

H = H % 12

H = float(H)
M = float(M)
S = float(S)

M_to_H = M / 60
S_to_H = S / (60*60)

clock_part = ((H + M_to_H + S_to_H)/12)*360

print ('Angle: {} degrees'.format(clock_part))
