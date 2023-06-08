def check_type(choose_type):
    def decorate(func):
        def wrapper(*args):
            num = []
            for arg in args:
                if choose_type == "int":
                    num.append(float(arg))
                elif choose_type == "str":
                    num.append(str(arg))
            return func(*num)

        return wrapper

    return decorate


@check_type("int")
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols(5, 6, 7))


@check_type("int")
def add_three_symbols2(a, b, c):
    return a + b + c


print(add_three_symbols2("3", 5, 0))


@check_type("int")
def add_three_symbols3(a, b, c):
    return a + b + c


print(add_three_symbols3(0.1, 0.2, 0.4))
