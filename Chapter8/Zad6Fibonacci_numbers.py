'''

'''

def fib_recurrent(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recurrent(n-2) + fib_recurrent(n-1)

def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        before_last, last = 0, 1
        for _ in range(2, n+1):
            last, before_last = last + before_last, last
            print(last)
        return last

print(fib_iter(5000))
for i in range(10):
    print(i, fib_iter(i))

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
