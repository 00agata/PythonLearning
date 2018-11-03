fint = int(input('Provide integer: '))

fract = 1
for i in range (1, fint+1):
    fract = fract * i

print('Fractional: {}'.format(fract))
