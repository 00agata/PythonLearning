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
    result = var_1 / var_2
    return result


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


welcome()
while True:

    option = raw_input("Enter option:")

    if option == "a":
        print("ADDING")
        add_var_1 = int(input("Input 1st operand:"))
        add_var_2 = int(input("Input 2nd operand:"))
        print("Result: {}".format(adding(add_var_1,add_var_2)))
    elif option == "s":
        print("SUBTRACT")
        add_var_1 = int(input("Input 1st operand:"))
        add_var_2 = int(input("Input 2nd operand:"))
        print("Result: {}".format(subtract(add_var_1, add_var_2)))
    elif option == "m":
        print("MULTIPLY")
        add_var_1 = int(input("Input 1st operand:"))
        add_var_2 = int(input("Input 2nd operand:"))
        print("Result: {}".format(multiply(add_var_1, add_var_2)))
    elif option == "d":
        print("DIVIDE")
        add_var_1 = int(input("Input 1st operand:"))
        add_var_2 = int(input("Input 2nd operand:"))
        print("Result: {}".format(divide(add_var_1, add_var_2)))
    elif option == "p":
        print("POWER")
        add_var_1 = int(input("Input 1st operand:"))
        add_var_2 = int(input("Input 2nd operand:"))
        print("Result: {}".format(power(add_var_1, add_var_2)))
    elif option == "h" or option == "?":
        help()
    elif option == "q":
        print("GOOD BYE")
        break
