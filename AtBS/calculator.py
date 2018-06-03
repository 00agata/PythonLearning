# Calculator


def adding(var_1, var_2):
    result = var_1 + var_2
    return result


def subtract(var_1, var_2):
    result = var_1 - var_2
    return result


def multiply(var_1, var_2):
    result = var_1 * var_2
    return result


def divide(var_1, var_2):
    if var_2 != 0:
        result = var_1 / var_2
        return result
    else:
        print('Not possible to be done. ZeroDivisionError.')


def power(var_1, var_2):
    result = var_1 ** var_2
    return result


def help():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def welcome():
    print("Welcome to badly organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def read_operands():
    variable_1 = int(input("Input 1st operand:"))
    variable_2 = int(input("Input 2nd operand:"))
    return (variable_1, variable_2)


welcome()

while True:
    try:
        option = raw_input("Enter option:")

        if option == "a":
            print("ADDING")
            (var_1, var_2) = read_operands()
            print("Result: {}".format(adding(var_1, var_2)))
        elif option == "s":
            print("SUBTRACT")
            (var_1, var_2) = read_operands()
            print("Result: {}".format(subtract(var_1, var_2)))
        elif option == "m":
            print("MULTIPLY")
            (var_1, var_2) = read_operands()
            print("Result: {}".format(multiply(var_1, var_2)))
        elif option == "d":
            print("DIVIDE")
            (var_1, var_2) = read_operands()
            print("Result: {}".format(divide(var_1, var_2)))
        elif option == "p":
            print("POWER")
            (var_1, var_2) = read_operands()
            print("Result: {}".format(power(var_1, var_2)))
        elif option == "h" or option == "?":
            help()
        elif option == "q":
            print("GOOD BYE")
            break
    except NameError:
        print('Invalid input value!')
