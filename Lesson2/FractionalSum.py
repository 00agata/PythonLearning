fint = int(input('Provide integer: '))

fract = 1
fract_sum = 0
for i in range (1, fint+1):
    fract = fract * i
    fract_sum = fract_sum + fract

print('Fractional: {}'.format(fract_sum))
