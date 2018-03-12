'''

'''


def fib(n):
    a = []
    a1 = 1  # id 1
    a2 = 1  # id 2
    a.append(a1)
    a.append(a2)

    if n == 1:
        return a1
    elif n == 2:
        return a2
    elif n > 2:
        print(a[a1])
        print(a[a2])
        for i in range(2, n):
            an = a[i-2] + a[i-1]
            a.append(an)
            print(an)
        return an
    else:
        print('Incorrect input values')


try:
    n = int(input('Input a positive integer n: '))
    fibonacci_nth = fib(n)
    print('Fib nth: {}'.format(fibonacci_nth))
except NameError:
    print ('Incorrect Input Value. Program finished')
