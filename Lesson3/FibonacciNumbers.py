

def fib(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n-1) + fib(n-2)



while(True):
    number = int(input('Please provide positive integer: '))
    if number < 0:
        break
    print(fib(number))
